/**
 * SciMaster Gr.6 — Score Store (client)
 *
 * - Student identity (name / student ID / class) kept in localStorage
 * - Every submitted exam = one attempt record (multiple attempts per subject kept)
 * - Attempts are saved locally first, then sent to Google Sheets (Apps Script).
 *   Failed sends stay in a queue and are retried on next load / when back online.
 * - "My history" view for the student, "Teacher dashboard" behind the Admin PIN.
 *
 * Depends on globals from app.js: state, showAdminAuthModal
 */
(function () {
  const CFG = window.SCIMASTER_CONFIG || {};
  const API = String(CFG.SCORE_API_URL || '').trim();

  const KEYS = {
    student: 'scimaster_student_profile',
    history: 'scimaster_attempt_history',
    queue: 'scimaster_attempt_queue',
    adminKey: 'scimaster_sheet_admin_key'
  };

  const SUBJECT_LABELS = {
    science: 'วิทยาศาสตร์', math: 'คณิตศาสตร์', thai: 'ภาษาไทย', programming: 'Coding & CT',
    chinese: 'ภาษาจีน', english: 'ภาษาอังกฤษ', math_en: 'Math (EN)', sci_en: 'Science (EN)',
    grammar: 'Grammar', phonics: 'Phonics', reading_writing: 'Reading & Writing',
    social: 'สังคมศึกษา', history: 'ประวัติศาสตร์', arduino: 'Arduino'
  };

  const $ = (id) => document.getElementById(id);

  // ---------- storage helpers ----------
  function readJSON(key, fallback) {
    try { const v = JSON.parse(localStorage.getItem(key)); return v ?? fallback; } catch { return fallback; }
  }
  function writeJSON(key, val) { localStorage.setItem(key, JSON.stringify(val)); }

  function getStudent() { return readJSON(KEYS.student, null); }
  function setStudent(p) { writeJSON(KEYS.student, p); }

  function uuid() {
    if (window.crypto && crypto.randomUUID) return crypto.randomUUID();
    return Date.now().toString(36) + '-' + Math.random().toString(36).slice(2, 10);
  }

  function esc(s) {
    return String(s ?? '').replace(/[&<>"']/g, c =>
      ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  }

  const normId = (v) => String(v || '').trim().toLowerCase();

  function fmtDate(iso) {
    const d = new Date(iso);
    if (isNaN(d)) return '-';
    return d.toLocaleString('th-TH', { dateStyle: 'short', timeStyle: 'short' });
  }
  function fmtTime(sec) {
    sec = Number(sec) || 0;
    return `${Math.floor(sec / 60)}:${String(sec % 60).padStart(2, '0')}`;
  }

  // ---------- network ----------
  async function apiPost(rec) {
    const res = await fetch(API, {
      method: 'POST',
      // text/plain keeps this a "simple" request, so Apps Script needs no CORS preflight
      headers: { 'Content-Type': 'text/plain;charset=utf-8' },
      body: JSON.stringify(rec)
    });
    const j = await res.json();
    if (!j.ok) throw new Error(j.error || 'Save failed');
    return j;
  }

  async function apiGet(params) {
    const url = API + '?' + new URLSearchParams(params).toString();
    const res = await fetch(url);
    const j = await res.json();
    if (!j.ok) throw new Error(j.error || 'Request failed');
    return j;
  }

  let flushing = false;
  async function flushQueue() {
    if (!API || flushing) return;
    flushing = true;
    try {
      let queue = readJSON(KEYS.queue, []);
      for (const rec of [...queue]) {
        try {
          const j = await apiPost(rec);
          queue = queue.filter(q => q.attemptId !== rec.attemptId);
          writeJSON(KEYS.queue, queue);
          const hist = readJSON(KEYS.history, []);
          const h = hist.find(x => x.attemptId === rec.attemptId);
          if (h) { h.synced = true; if (j.attemptNo) h.attemptNo = j.attemptNo; writeJSON(KEYS.history, hist); }
          setSyncStatus(rec.attemptId, 'synced');
        } catch (err) {
          console.warn('Score sync failed, will retry later:', err);
          setSyncStatus(rec.attemptId, 'queued');
          break; // offline or server error: stop and keep the rest queued
        }
      }
    } finally {
      flushing = false;
    }
  }

  // ---------- record an attempt (called by app.js submitExam) ----------
  let lastAttemptId = null;

  function recordAttempt(result) {
    const s = getStudent() || {};
    const hist = readJSON(KEYS.history, []);
    const localAttemptNo = hist.filter(h =>
      normId(h.studentId) === normId(s.studentId) && h.subject === result.subject).length + 1;

    const rec = {
      attemptId: uuid(),
      submittedAt: new Date().toISOString(),
      studentId: s.studentId || 'unknown',
      studentName: s.studentName || 'ไม่ระบุชื่อ',
      classRoom: s.classRoom || '',
      subject: result.subject,
      subjectTitle: result.subjectTitle || SUBJECT_LABELS[result.subject] || result.subject,
      attemptNo: localAttemptNo,
      totalScore: result.totalScore,
      maxScore: result.maxScore,
      percent: result.percent,
      passed: !!result.passed,
      secA: result.secA, secB: result.secB, secC: result.secC, secD: result.secD,
      timeSpentSec: result.timeSpentSec,
      answeredCount: result.answeredCount,
      totalQuestions: result.totalQuestions
    };

    hist.push({ ...rec, synced: false });
    writeJSON(KEYS.history, hist);

    lastAttemptId = rec.attemptId;
    if (API) {
      const queue = readJSON(KEYS.queue, []);
      queue.push(rec);
      writeJSON(KEYS.queue, queue);
      setSyncStatus(rec.attemptId, 'sending');
      flushQueue();
    } else {
      setSyncStatus(rec.attemptId, 'local');
    }
    return rec;
  }

  function setSyncStatus(attemptId, status) {
    if (attemptId !== lastAttemptId) return;
    const el = $('scoreSyncStatus');
    if (!el) return;
    const s = getStudent() || {};
    const who = `${esc(s.studentName || '')} (${esc(s.studentId || '-')}${s.classRoom ? ' · ' + esc(s.classRoom) : ''})`;
    const map = {
      sending: ['sync-sending', 'fa-solid fa-spinner fa-spin', `กำลังบันทึกคะแนนของ ${who}...`],
      synced: ['sync-ok', 'fa-solid fa-cloud-arrow-up', `บันทึกคะแนนของ ${who} ลง Google Sheets แล้ว`],
      queued: ['sync-warn', 'fa-solid fa-wifi', `บันทึกในเครื่องแล้ว ยังส่งขึ้นระบบไม่ได้ จะส่งอีกครั้งอัตโนมัติเมื่อออนไลน์`],
      local: ['sync-warn', 'fa-solid fa-hard-drive', `บันทึกคะแนนของ ${who} ไว้ในเครื่องนี้ (ยังไม่ได้ตั้งค่า Google Sheets)`]
    };
    const [cls, icon, text] = map[status] || map.local;
    el.className = 'score-sync-status ' + cls;
    el.innerHTML = `<i class="${icon}"></i> ${text}`;
    el.style.display = 'flex';
  }

  // ---------- student identity ----------
  function renderStudentBadge() {
    const s = getStudent();
    const label = $('studentBadgeLabel');
    if (!label) return;
    label.textContent = s ? `${s.studentName} · ${s.classRoom || s.studentId}` : 'ลงชื่อเข้าสอบ';
  }

  let resumeTimerAfterLogin = false;

  function openStudentModal(force) {
    const s = getStudent();
    $('studentNameInput').value = s?.studentName || '';
    $('studentIdInput').value = s?.studentId || '';
    $('studentClassInput').value = s?.classRoom || '';
    $('studentLoginError').style.display = 'none';
    $('closeStudentModal').style.display = force ? 'none' : '';
    $('switchStudentBtn').style.display = s ? '' : 'none';
    if (typeof state !== 'undefined' && !state.timerPaused) {
      state.timerPaused = true;
      resumeTimerAfterLogin = true;
    }
    $('studentLoginModal').style.display = 'flex';
    setTimeout(() => $('studentNameInput').focus(), 100);
  }

  function closeStudentModal() {
    $('studentLoginModal').style.display = 'none';
    if (resumeTimerAfterLogin && typeof state !== 'undefined') {
      state.timerPaused = false;
      resumeTimerAfterLogin = false;
    }
  }

  function saveStudentFromForm() {
    const name = $('studentNameInput').value.trim();
    const id = $('studentIdInput').value.trim();
    const cls = $('studentClassInput').value.trim();
    if (!name || !id || !cls) {
      $('studentLoginError').style.display = 'flex';
      return;
    }
    const prev = getStudent();
    if (prev && normId(prev.studentId) !== normId(id)) {
      // A different student on a shared device must not inherit the previous answers
      if (!confirm('รหัสนักเรียนเปลี่ยนไป ระบบจะล้างคำตอบที่ค้างอยู่ของนักเรียนคนก่อนในเครื่องนี้ ต้องการดำเนินการต่อหรือไม่?')) return;
      clearExamProgress();
      setStudent({ studentName: name, studentId: id, classRoom: cls });
      location.reload();
      return;
    }
    setStudent({ studentName: name, studentId: id, classRoom: cls });
    renderStudentBadge();
    closeStudentModal();
  }

  function switchStudent() {
    if (!confirm('ออกจากระบบนักเรียนคนนี้? คำตอบที่ยังไม่ส่งในเครื่องนี้จะถูกล้าง (ประวัติคะแนนที่ส่งแล้วยังอยู่)')) return;
    clearExamProgress();
    localStorage.removeItem(KEYS.student);
    location.reload();
  }

  function clearExamProgress() {
    Object.keys(localStorage)
      .filter(k => k.endsWith('_exam_state_v1') || k.endsWith('_exam_result_v1'))
      .forEach(k => localStorage.removeItem(k));
  }

  // ---------- tables ----------
  function attemptRowHTML(a, withStudent) {
    const pct = Number(a.percent) || 0;
    const passed = a.passed === true || a.passed === 'true' || a.passed === 'TRUE';
    return `<tr>
      <td>${esc(fmtDate(a.submittedAt))}</td>
      ${withStudent ? `<td>${esc(a.studentId)}</td><td>${esc(a.studentName)}</td><td>${esc(a.classRoom)}</td>` : ''}
      <td>${esc(a.subjectTitle || SUBJECT_LABELS[a.subject] || a.subject)}</td>
      <td class="num">#${esc(a.attemptNo)}</td>
      <td class="num"><strong>${esc(a.totalScore)}</strong>/${esc(a.maxScore)}</td>
      <td class="num">${pct.toFixed(1)}%</td>
      <td><span class="pass-chip ${passed ? 'pass' : 'fail'}">${passed ? 'ผ่าน' : 'ไม่ผ่าน'}</span></td>
      <td class="num">${esc(a.secA)}/${esc(a.secB)}/${esc(a.secC)}/${esc(a.secD)}</td>
      <td class="num">${fmtTime(a.timeSpentSec)}</td>
      ${withStudent ? '' : `<td>${a.synced === false ? '<i class="fa-solid fa-clock-rotate-left" title="รอส่งขึ้นระบบ"></i>' : '<i class="fa-solid fa-check" title="บันทึกแล้ว"></i>'}</td>`}
    </tr>`;
  }

  // ---------- my history ----------
  async function openHistory() {
    const s = getStudent();
    if (!s) { openStudentModal(false); return; }
    $('historyStudentInfo').textContent = `${s.studentName} · รหัส ${s.studentId} · ${s.classRoom}`;
    $('historyModal').style.display = 'flex';

    const local = readJSON(KEYS.history, []).filter(a => normId(a.studentId) === normId(s.studentId));
    renderHistory(local, API ? 'กำลังโหลดประวัติจากระบบ...' : 'แสดงเฉพาะประวัติในเครื่องนี้');

    if (!API) return;
    try {
      const j = await apiGet({ action: 'student', studentId: s.studentId });
      // merge: server rows + local rows not yet on the server
      const serverIds = new Set(j.attempts.map(a => a.attemptId));
      const merged = [...j.attempts.map(a => ({ ...a, synced: true })), ...local.filter(a => !serverIds.has(a.attemptId))];
      renderHistory(merged, '');
    } catch (err) {
      renderHistory(local, 'โหลดจากระบบไม่ได้ แสดงเฉพาะประวัติในเครื่องนี้');
    }
  }

  function renderHistory(list, note) {
    list = [...list].sort((a, b) => new Date(b.submittedAt) - new Date(a.submittedAt));
    $('historyNote').textContent = note || '';
    $('historyNote').style.display = note ? 'block' : 'none';
    $('historyTableBody').innerHTML = list.length
      ? list.map(a => attemptRowHTML(a, false)).join('')
      : `<tr><td colspan="9" class="empty-row">ยังไม่มีประวัติการสอบ</td></tr>`;

    // best score per subject
    const best = {};
    list.forEach(a => {
      const k = a.subject;
      if (!best[k] || Number(a.percent) > Number(best[k].percent)) best[k] = a;
    });
    $('historyBestCards').innerHTML = Object.values(best).map(a => `
      <div class="best-card">
        <div class="best-subject">${esc(a.subjectTitle || SUBJECT_LABELS[a.subject] || a.subject)}</div>
        <div class="best-score">${esc(a.totalScore)}<span>/${esc(a.maxScore)}</span></div>
        <div class="best-meta">สูงสุด ${(Number(a.percent) || 0).toFixed(1)}% · สอบ ${list.filter(x => x.subject === a.subject).length} ครั้ง</div>
      </div>`).join('');
  }

  // ---------- teacher dashboard ----------
  let dashboardData = [];

  function requestDashboard() {
    if (typeof state !== 'undefined' && state.isAdmin) { openDashboard(); return; }
    state.adminAuthPurpose = 'dashboard';
    showAdminAuthModal();
  }

  async function openDashboard() {
    $('dashboardModal').style.display = 'flex';
    $('dashboardKeyRow').style.display = API ? 'flex' : 'none';
    $('dashboardKeyInput').value = sessionStorage.getItem(KEYS.adminKey) || '';
    await loadDashboard();
  }

  async function loadDashboard() {
    const note = $('dashboardNote');
    const local = readJSON(KEYS.history, []);

    if (!API) {
      dashboardData = local;
      note.innerHTML = '<i class="fa-solid fa-circle-info"></i> ยังไม่ได้ตั้งค่า Google Sheets (config.js) แสดงเฉพาะผลสอบที่ทำในเครื่องนี้';
      note.style.display = 'flex';
      renderDashboard();
      return;
    }

    const key = sessionStorage.getItem(KEYS.adminKey) || '';
    if (!key) {
      dashboardData = local;
      note.innerHTML = '<i class="fa-solid fa-key"></i> กรอก Sheet Admin Key เพื่อดูผลสอบของนักเรียนทุกคน (ตอนนี้แสดงเฉพาะเครื่องนี้)';
      note.style.display = 'flex';
      renderDashboard();
      return;
    }

    note.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> กำลังโหลดข้อมูลจาก Google Sheets...';
    note.style.display = 'flex';
    try {
      const j = await apiGet({ action: 'all', key });
      dashboardData = j.attempts;
      note.style.display = 'none';
    } catch (err) {
      dashboardData = local;
      note.innerHTML = `<i class="fa-solid fa-triangle-exclamation"></i> โหลดไม่สำเร็จ: ${esc(err.message)} (แสดงเฉพาะเครื่องนี้)`;
    }
    populateFilters();
    renderDashboard();
  }

  function populateFilters() {
    const subjSel = $('dashSubjectFilter');
    const clsSel = $('dashClassFilter');
    const curS = subjSel.value, curC = clsSel.value;
    const subjects = [...new Set(dashboardData.map(a => a.subject))].sort();
    const classes = [...new Set(dashboardData.map(a => a.classRoom).filter(Boolean))].sort();
    subjSel.innerHTML = '<option value="">ทุกวิชา</option>' +
      subjects.map(s => `<option value="${esc(s)}">${esc(SUBJECT_LABELS[s] || s)}</option>`).join('');
    clsSel.innerHTML = '<option value="">ทุกห้อง</option>' +
      classes.map(c => `<option value="${esc(c)}">${esc(c)}</option>`).join('');
    subjSel.value = subjects.includes(curS) ? curS : '';
    clsSel.value = classes.includes(curC) ? curC : '';
  }

  function filteredDashboard() {
    const subj = $('dashSubjectFilter').value;
    const cls = $('dashClassFilter').value;
    const q = $('dashSearch').value.trim().toLowerCase();
    const latestOnly = $('dashLatestOnly').checked;

    let rows = dashboardData.filter(a =>
      (!subj || a.subject === subj) &&
      (!cls || a.classRoom === cls) &&
      (!q || String(a.studentName).toLowerCase().includes(q) || String(a.studentId).toLowerCase().includes(q))
    );

    if (latestOnly) {
      const latest = {};
      rows.forEach(a => {
        const k = normId(a.studentId) + '|' + a.subject;
        if (!latest[k] || new Date(a.submittedAt) > new Date(latest[k].submittedAt)) latest[k] = a;
      });
      rows = Object.values(latest);
    }
    return rows.sort((a, b) => new Date(b.submittedAt) - new Date(a.submittedAt));
  }

  function renderDashboard() {
    if (!$('dashSubjectFilter').options.length) populateFilters();
    const rows = filteredDashboard();

    const students = new Set(rows.map(a => normId(a.studentId))).size;
    const avg = rows.length ? rows.reduce((s, a) => s + (Number(a.percent) || 0), 0) / rows.length : 0;
    const passCount = rows.filter(a => a.passed === true || a.passed === 'true' || a.passed === 'TRUE').length;
    $('dashStatAttempts').textContent = rows.length;
    $('dashStatStudents').textContent = students;
    $('dashStatAvg').textContent = avg.toFixed(1) + '%';
    $('dashStatPass').textContent = rows.length ? Math.round(passCount / rows.length * 100) + '%' : '0%';

    $('dashboardTableBody').innerHTML = rows.length
      ? rows.map(a => attemptRowHTML(a, true)).join('')
      : `<tr><td colspan="11" class="empty-row">ไม่พบข้อมูล</td></tr>`;
  }

  function exportCSV() {
    const rows = filteredDashboard();
    const cols = ['submittedAt', 'studentId', 'studentName', 'classRoom', 'subject', 'subjectTitle', 'attemptNo',
      'totalScore', 'maxScore', 'percent', 'passed', 'secA', 'secB', 'secC', 'secD', 'timeSpentSec', 'answeredCount', 'totalQuestions'];
    const cell = (v) => {
      let s = String(v ?? '');
      if (/^[=+\-@]/.test(s)) s = "'" + s; // avoid formula injection when opened in Excel
      return /[",\n]/.test(s) ? `"${s.replace(/"/g, '""')}"` : s;
    };
    const csv = '\uFEFF' + [cols.join(','), ...rows.map(r => cols.map(c => cell(r[c])).join(','))].join('\n');
    const blob = new Blob([csv], { type: 'text/csv;charset=utf-8' });
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = `scimaster_scores_${new Date().toISOString().slice(0, 10)}.csv`;
    a.click();
    URL.revokeObjectURL(a.href);
  }

  // ---------- wiring ----------
  function init() {
    const dl = $('classOptions');
    if (dl) dl.innerHTML = (CFG.CLASS_OPTIONS || []).map(c => `<option value="${esc(c)}"></option>`).join('');

    renderStudentBadge();
    if (!getStudent()) openStudentModal(true);

    $('studentBadgeBtn')?.addEventListener('click', () => openStudentModal(false));
    $('saveStudentBtn')?.addEventListener('click', saveStudentFromForm);
    $('closeStudentModal')?.addEventListener('click', closeStudentModal);
    $('switchStudentBtn')?.addEventListener('click', switchStudent);
    ['studentNameInput', 'studentIdInput', 'studentClassInput'].forEach(id =>
      $(id)?.addEventListener('keydown', e => { if (e.key === 'Enter') { e.preventDefault(); saveStudentFromForm(); } }));

    $('myHistoryBtn')?.addEventListener('click', openHistory);
    $('closeHistoryModal')?.addEventListener('click', () => { $('historyModal').style.display = 'none'; });

    $('teacherDashboardBtn')?.addEventListener('click', requestDashboard);
    $('closeDashboardModal')?.addEventListener('click', () => { $('dashboardModal').style.display = 'none'; });
    $('dashRefreshBtn')?.addEventListener('click', loadDashboard);
    $('dashExportBtn')?.addEventListener('click', exportCSV);
    $('dashSaveKeyBtn')?.addEventListener('click', () => {
      sessionStorage.setItem(KEYS.adminKey, $('dashboardKeyInput').value.trim());
      loadDashboard();
    });
    ['dashSubjectFilter', 'dashClassFilter', 'dashLatestOnly'].forEach(id => $(id)?.addEventListener('change', renderDashboard));
    $('dashSearch')?.addEventListener('input', renderDashboard);

    window.addEventListener('online', flushQueue);
    flushQueue();
  }

  document.addEventListener('DOMContentLoaded', init);

  window.ScoreStore = { recordAttempt, openDashboard, openHistory, getStudent, flushQueue };
})();
