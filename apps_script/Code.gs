/**
 * SciMaster Gr.6 — Score Store backend (Google Apps Script Web App)
 *
 * Stores every exam attempt as one row in the "Attempts" sheet.
 * Deploy: Extensions > Apps Script > paste this file > Deploy > New deployment
 *         Type: Web app | Execute as: Me | Who has access: Anyone
 * Then set Script Property ADMIN_KEY (Project Settings > Script properties).
 * See SCORE_STORAGE_SETUP.md for the full guide.
 */

const SHEET_NAME = 'Attempts';

// Column order of the sheet. Do not reorder after data exists.
const HEADERS = [
  'attemptId', 'submittedAt', 'studentId', 'studentName', 'classRoom',
  'subject', 'subjectTitle', 'attemptNo',
  'totalScore', 'maxScore', 'percent', 'passed',
  'secA', 'secB', 'secC', 'secD',
  'timeSpentSec', 'answeredCount', 'totalQuestions', 'receivedAt'
];

// ---------- HTTP entry points ----------

/** Save one attempt. Body: JSON (sent as text/plain to avoid CORS preflight). */
function doPost(e) {
  const lock = LockService.getScriptLock();
  try {
    lock.waitLock(10000);
    const data = JSON.parse((e && e.postData && e.postData.contents) || '{}');

    const required = ['attemptId', 'studentId', 'studentName', 'subject'];
    for (const f of required) {
      if (!data[f] || String(data[f]).trim() === '') {
        return json_({ ok: false, error: 'Missing field: ' + f });
      }
    }

    const sheet = getSheet_();
    const rows = readRows_(sheet);

    // Idempotent: the client retries queued attempts, so ignore duplicates.
    const existing = rows.find(r => r.attemptId === data.attemptId);
    if (existing) {
      return json_({ ok: true, duplicate: true, attemptNo: existing.attemptNo });
    }

    // Server-side attempt number = previous attempts by this student in this subject + 1
    const studentId = normId_(data.studentId);
    const attemptNo = rows.filter(r =>
      normId_(r.studentId) === studentId && r.subject === data.subject
    ).length + 1;

    const record = {
      attemptId: data.attemptId,
      submittedAt: data.submittedAt || new Date().toISOString(),
      studentId: data.studentId,
      studentName: data.studentName,
      classRoom: data.classRoom || '',
      subject: data.subject,
      subjectTitle: data.subjectTitle || '',
      attemptNo: attemptNo,
      totalScore: num_(data.totalScore),
      maxScore: num_(data.maxScore),
      percent: num_(data.percent),
      passed: data.passed === true || data.passed === 'true',
      secA: num_(data.secA),
      secB: num_(data.secB),
      secC: num_(data.secC),
      secD: num_(data.secD),
      timeSpentSec: num_(data.timeSpentSec),
      answeredCount: num_(data.answeredCount),
      totalQuestions: num_(data.totalQuestions),
      receivedAt: new Date().toISOString()
    };

    sheet.appendRow(HEADERS.map(h => safeCell_(record[h])));
    return json_({ ok: true, attemptNo: attemptNo });
  } catch (err) {
    return json_({ ok: false, error: String(err) });
  } finally {
    try { lock.releaseLock(); } catch (e) { /* lock not held */ }
  }
}

/**
 * Read attempts.
 *   ?action=ping                         -> health check
 *   ?action=student&studentId=12345      -> one student's attempts
 *   ?action=all&key=ADMIN_KEY            -> every attempt (teacher dashboard)
 */
function doGet(e) {
  try {
    const p = (e && e.parameter) || {};
    const action = p.action || 'ping';

    if (action === 'ping') return json_({ ok: true, service: 'scimaster-score-store' });

    const rows = readRows_(getSheet_());

    if (action === 'student') {
      const id = normId_(p.studentId);
      if (!id) return json_({ ok: false, error: 'studentId required' });
      return json_({ ok: true, attempts: rows.filter(r => normId_(r.studentId) === id) });
    }

    if (action === 'all') {
      const adminKey = PropertiesService.getScriptProperties().getProperty('ADMIN_KEY');
      if (!adminKey) return json_({ ok: false, error: 'ADMIN_KEY is not set in Script properties' });
      if (p.key !== adminKey) return json_({ ok: false, error: 'Invalid admin key' });
      return json_({ ok: true, attempts: rows });
    }

    return json_({ ok: false, error: 'Unknown action' });
  } catch (err) {
    return json_({ ok: false, error: String(err) });
  }
}

// ---------- helpers ----------

function getSheet_() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sheet = ss.getSheetByName(SHEET_NAME);
  if (!sheet) sheet = ss.insertSheet(SHEET_NAME);
  if (sheet.getLastRow() === 0) {
    sheet.appendRow(HEADERS);
    sheet.setFrozenRows(1);
    sheet.getRange(1, 1, 1, HEADERS.length).setFontWeight('bold');
  }
  return sheet;
}

function readRows_(sheet) {
  const last = sheet.getLastRow();
  if (last < 2) return [];
  const values = sheet.getRange(2, 1, last - 1, HEADERS.length).getValues();
  return values.map(v => {
    const o = {};
    HEADERS.forEach((h, i) => {
      const val = v[i];
      o[h] = val instanceof Date ? val.toISOString() : val;
    });
    return o;
  });
}

function normId_(v) { return String(v || '').trim().toLowerCase(); }

function num_(v) {
  const n = Number(v);
  return isFinite(n) ? n : 0;
}

/** Block spreadsheet formula injection from user-typed text (=, +, -, @). */
function safeCell_(v) {
  if (typeof v === 'string' && /^[=+\-@]/.test(v)) return "'" + v;
  return v;
}

function json_(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}
