/**
 * SciMaster / MathMaster Gr.6 - Interactive Exam Portal Engine
 * Multi-subject support (Science & Mathematics), State management, LocalStorage auto-save, scoring & analytics.
 */

// Global State
const state = {
  currentSubject: localStorage.getItem('scimaster_selected_subject') || 'science', // 'science', 'math', 'thai', 'programming'
  questions: [],
  meta: {},
  currentIndex: 0,
  userAnswers: {},     // { questionId: answerValue }
  bookmarks: new Set(),
  activeSectionFilter: 'ALL',
  paletteFilter: 'all', // 'all', 'unanswered', 'bookmarked'

  timerSeconds: 3600,  // 60 minutes
  timerInterval: null,
  timerPaused: false,
  timeSpentSeconds: 0,
  isSubmitted: false
};

// Storage Keys Generator
function getStorageKeys() {
  const prefix = state.currentSubject === 'math' ? 'mathmaster_gr6'
               : state.currentSubject === 'thai' ? 'thaimaster_gr6'
               : state.currentSubject === 'programming' ? 'coding_gr6'
               : state.currentSubject === 'chinese' ? 'chinese_gr6'
               : state.currentSubject === 'english' ? 'english_gr6'
               : 'scimaster_gr6';
  return {
    STORAGE_KEY: `${prefix}_exam_state_v1`,
    RESULT_KEY: `${prefix}_exam_result_v1`
  };
}

// DOM Elements
const brandBadge = document.getElementById('brandBadge');
const brandIcon = document.getElementById('brandIcon');
const brandTitle = document.getElementById('brandTitle');
const portalTitle = document.getElementById('portalTitle');
const subSciBtn = document.getElementById('subSciBtn');
const subMathBtn = document.getElementById('subMathBtn');
const subThaiBtn = document.getElementById('subThaiBtn');
const subProgBtn = document.getElementById('subProgBtn');
const subChineseBtn = document.getElementById('subChineseBtn');
const subEngBtn = document.getElementById('subEngBtn');

const qSectionBadge = document.getElementById('qSectionBadge');
const qTopicBadge = document.getElementById('qTopicBadge');
const qDiffBadge = document.getElementById('qDiffBadge');
const qLoBadge = document.getElementById('qLoBadge');
const qPointsBadge = document.getElementById('qPointsBadge');
const bookmarkBtn = document.getElementById('bookmarkBtn');
const scenarioContainer = document.getElementById('scenarioContainer');
const scenarioText = document.getElementById('scenarioText');
const qNumberDisplay = document.getElementById('qNumberDisplay');
const qTextDisplay = document.getElementById('qTextDisplay');
const answerContainer = document.getElementById('answerContainer');
const explanationBox = document.getElementById('explanationBox');
const expCorrectAnswer = document.getElementById('expCorrectAnswer');
const expText = document.getElementById('expText');

const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');

const questionGrid = document.getElementById('questionGrid');

const answeredCount = document.getElementById('answeredCount');
const overallProgressBar = document.getElementById('overallProgressBar');
const timerDisplay = document.getElementById('timerDisplay');
const toggleTimerBtn = document.getElementById('toggleTimerBtn');
const editTimerBtn = document.getElementById('editTimerBtn');
const finishExamBtn = document.getElementById('finishExamBtn');

const resultModal = document.getElementById('resultModal');
const closeResultModal = document.getElementById('closeResultModal');
const summaryModal = document.getElementById('summaryModal');
const closeSummaryModal = document.getElementById('closeSummaryModal');
const summaryNotesBtn = document.getElementById('summaryNotesBtn');
const resetSessionBtn = document.getElementById('resetSessionBtn');
const reviewAllAnswersBtn = document.getElementById('reviewAllAnswersBtn');
const retryExamBtn = document.getElementById('retryExamBtn');

// Initialize Application
async function init() {
  updateSubjectThemeUI();
  
  const dataFile = state.currentSubject === 'math' ? 'quiz_math_data.json'
               : state.currentSubject === 'thai' ? 'quiz_thai_data.json'
               : state.currentSubject === 'programming' ? 'quiz_programming_data.json'
               : state.currentSubject === 'chinese' ? 'quiz_chinese_data.json'
               : state.currentSubject === 'english' ? 'quiz_english_data.json'
               : 'quiz_data.json';
  
  try {
    const res = await fetch(dataFile);
    const data = await res.json();
    state.questions = data.questions;
    state.meta = data.meta;

    loadSavedState();
    setupEventListeners();

    // If exam was already submitted before the server reset, restore the result
    const { RESULT_KEY } = getStorageKeys();
    const savedResult = localStorage.getItem(RESULT_KEY);
    if (savedResult && state.isSubmitted) {
      try {
        const r = JSON.parse(savedResult);
        restoreResultModal(r);
      } catch (e) {
        console.warn('Could not restore result:', e);
      }
      return; // Don't restart timer or re-render exam
    }

    startTimer();
    renderQuestionGrid();
    renderCurrentQuestion();
    updateProgressUI();
  } catch (err) {
    console.error('Failed to load quiz data:', err);
    qTextDisplay.innerText = 'เกิดข้อผิดพลาดในการโหลดข้อสอบ กรุณารีเฟรชหน้านี้ใหม่';
  }
}

// Switch Subject Function
function switchSubject(newSubject) {
  if (state.currentSubject === newSubject) return;
  
  // Save current subject state first
  saveState();
  if (state.timerInterval) clearInterval(state.timerInterval);

  state.currentSubject = newSubject;
  localStorage.setItem('scimaster_selected_subject', newSubject);

  // Reset in-memory state for fresh load
  state.currentIndex = 0;
  state.userAnswers = {};
  state.bookmarks.clear();
  state.activeSectionFilter = 'ALL';
  state.paletteFilter = 'all';

  state.timerSeconds = 3600;
  state.timerPaused = false;
  state.timeSpentSeconds = 0;
  state.isSubmitted = false;

  // Re-run init with new subject
  init();
}

function updateSubjectThemeUI() {
  // Remove active from all pills first
  [subSciBtn, subMathBtn, subThaiBtn, subProgBtn, subChineseBtn, subEngBtn].forEach(btn => {
    if (btn) btn.classList.remove('active', 'math-theme', 'thai-theme', 'programming-theme', 'chinese-theme', 'english-theme');
  });

  if (state.currentSubject === 'math') {
    if (subMathBtn) { subMathBtn.classList.add('active', 'math-theme'); }
    if (brandTitle) brandTitle.innerText = 'MATHMASTER GR.6';
    if (brandIcon) brandIcon.className = 'fa-solid fa-calculator pulse-icon';
    if (portalTitle) portalTitle.innerText = 'ระบบทดสอบวัดผลการเรียนรู้คณิตศาสตร์ ป.6';
    document.title = 'MathMaster Gr.6 - ข้อสอบประเมินผลคณิตศาสตร์ ป.6 ฉบับออนไลน์';
  } else if (state.currentSubject === 'thai') {
    if (subThaiBtn) { subThaiBtn.classList.add('active', 'thai-theme'); }
    if (brandTitle) brandTitle.innerText = 'THAIMASTER GR.6';
    if (brandIcon) brandIcon.className = 'fa-solid fa-book pulse-icon';
    if (portalTitle) portalTitle.innerText = 'ระบบทดสอบวัดผลการเรียนรู้ภาษาไทย ป.6';
    document.title = 'ThaiMaster Gr.6 - ข้อสอบประเมินผลภาษาไทย ป.6 ฉบับออนไลน์';
  } else if (state.currentSubject === 'programming') {
    if (subProgBtn) { subProgBtn.classList.add('active', 'programming-theme'); }
    if (brandTitle) brandTitle.innerText = 'CODEMASTER GR.6';
    if (brandIcon) brandIcon.className = 'fa-solid fa-code pulse-icon';
    if (portalTitle) portalTitle.innerText = 'ระบบทดสอบวัดผลการเรียนรู้เทคโนโลยีการคำนวณ ป.6';
    document.title = 'CodeMaster Gr.6 - ข้อสอบประเมินผลเทคโนโลยีการคำนวณ ป.6 ฉบับออนไลน์';
  } else if (state.currentSubject === 'chinese') {
    if (subChineseBtn) { subChineseBtn.classList.add('active', 'chinese-theme'); }
    if (brandTitle) brandTitle.innerText = 'CHINESEMASTER GR.6';
    if (brandIcon) brandIcon.className = 'fa-solid fa-dragon pulse-icon';
    if (portalTitle) portalTitle.innerText = 'ระบบทดสอบวัดผลการเรียนรู้ภาษาจีน ป.6';
    document.title = 'ChineseMaster Gr.6 - ข้อสอบประเมินผลภาษาจีน ป.6 ฉบับออนไลน์';
  } else if (state.currentSubject === 'english') {
    if (subEngBtn) { subEngBtn.classList.add('active', 'english-theme'); }
    if (brandTitle) brandTitle.innerText = 'ENGLISHMASTER GR.6';
    if (brandIcon) brandIcon.className = 'fa-solid fa-language pulse-icon';
    if (portalTitle) portalTitle.innerText = 'ระบบทดสอบวัดผลการเรียนรู้ภาษาอังกฤษ ป.6';
    document.title = 'EnglishMaster Gr.6 - ข้อสอบประเมินผลภาษาอังกฤษ ป.6 ฉบับออนไลน์';
  } else {
    if (subSciBtn) { subSciBtn.classList.add('active'); }
    if (brandTitle) brandTitle.innerText = 'SCIMASTER GR.6';
    if (brandIcon) brandIcon.className = 'fa-solid fa-atom pulse-icon';
    if (portalTitle) portalTitle.innerText = 'ระบบทดสอบวัดผลการเรียนรู้วิทยาศาสตร์ ป.6';
    document.title = 'SciMaster Gr.6 - ข้อสอบประเมินผลวิทยาศาสตร์ ป.6 ฉบับออนไลน์';
  }
}

// Restore result modal from saved result data (after server reset)
function restoreResultModal(r) {
  state.isSubmitted = true;
  document.getElementById('resTotalScore').innerText = r.totalScore;
  const statusEl = document.getElementById('resPassStatus');
  if (r.isPassed) {
    statusEl.className = 'status-pass';
    statusEl.innerHTML = '<i class="fa-solid fa-circle-check"></i> ยินดีด้วย! ผ่านเกณฑ์ระดับยอดเยี่ยม';
  } else {
    statusEl.className = 'status-fail';
    statusEl.innerHTML = '<i class="fa-solid fa-triangle-exclamation"></i> ยังไม่ผ่านเกณฑ์ 80% (ควรทบทวนเพิ่มเติม)';
  }
  const maxScore = state.meta.totalScore || 150;
  const pct = ((r.totalScore / maxScore) * 100).toFixed(1);
  document.getElementById('resPercentage').innerText = `คิดเป็น ${pct}% (เกณฑ์ผ่าน 80% = ${state.meta.passingScore} คะแนน)`;
  const mins = Math.floor(r.timeSpentSeconds / 60);
  const secs = r.timeSpentSeconds % 60;
  document.getElementById('resTimeSpent').innerHTML = `<i class="fa-regular fa-clock"></i> ใช้เวลาทำข้อสอบ: ${mins} นาที ${secs} วินาที`;
  document.getElementById('scoreSecA').innerText = `${r.secAScore}/60`;
  document.getElementById('pctSecA').innerText  = `${Math.round((r.secAScore/60)*100)}%`;
  document.getElementById('barSecA').style.width = `${(r.secAScore/60)*100}%`;
  document.getElementById('scoreSecB').innerText = `${r.secBScore}/30`;
  document.getElementById('pctSecB').innerText  = `${Math.round((r.secBScore/30)*100)}%`;
  document.getElementById('barSecB').style.width = `${(r.secBScore/30)*100}%`;
  document.getElementById('scoreSecC').innerText = `${r.secCScore}/30`;
  document.getElementById('pctSecC').innerText  = `${Math.round((r.secCScore/30)*100)}%`;
  document.getElementById('barSecC').style.width = `${(r.secCScore/30)*100}%`;
  document.getElementById('scoreSecD').innerText = `${r.secDScore}/30`;
  document.getElementById('pctSecD').innerText  = `${Math.round((r.secDScore/30)*100)}%`;
  document.getElementById('barSecD').style.width = `${(r.secDScore/30)*100}%`;
  resultModal.style.display = 'flex';
}

// LocalStorage Persistence
function saveState() {
  const { STORAGE_KEY } = getStorageKeys();
  const serialized = {
    userAnswers: state.userAnswers,
    bookmarks: Array.from(state.bookmarks),
    currentIndex: state.currentIndex,
    timerSeconds: state.timerSeconds,
    timeSpentSeconds: state.timeSpentSeconds,

    isSubmitted: state.isSubmitted,
    savedAt: Date.now() // Track real-world save timestamp
  };
  localStorage.setItem(STORAGE_KEY, JSON.stringify(serialized));
}

// Save final graded result separately so it survives a server reset
function saveResult(result) {
  const { RESULT_KEY } = getStorageKeys();
  localStorage.setItem(RESULT_KEY, JSON.stringify({
    ...result,
    submittedAt: Date.now()
  }));
}

function loadSavedState() {
  const { STORAGE_KEY } = getStorageKeys();
  const saved = localStorage.getItem(STORAGE_KEY);
  if (!saved) return;
  try {
    const parsed = JSON.parse(saved);
    state.userAnswers = parsed.userAnswers || {};
    state.bookmarks = new Set(parsed.bookmarks || []);
    state.currentIndex = parsed.currentIndex || 0;

    state.timeSpentSeconds = parsed.timeSpentSeconds || 0;
    state.isSubmitted = parsed.isSubmitted || false;

    // Adjust timer for real elapsed time during server downtime / page close
    const savedTimer = parsed.timerSeconds ?? 3600;
    if (parsed.savedAt && savedTimer > 0) {
      const elapsedSinceSave = Math.floor((Date.now() - parsed.savedAt) / 1000);
      state.timerSeconds = Math.max(0, savedTimer - elapsedSinceSave);
      state.timeSpentSeconds += Math.min(elapsedSinceSave, savedTimer);
    } else {
      state.timerSeconds = savedTimer;
    }


  } catch (e) {
    console.warn('Could not parse saved state:', e);
  }
}

// Timer Logic
function startTimer() {
  if (state.timerInterval) clearInterval(state.timerInterval);
  updateTimerUI();
  state.timerInterval = setInterval(() => {
    if (!state.timerPaused && !state.isSubmitted) {
      if (state.timerSeconds > 0) {
        state.timerSeconds--;
        state.timeSpentSeconds++;
        updateTimerUI();
        if (state.timerSeconds % 10 === 0) saveState();
      } else {
        clearInterval(state.timerInterval);
        alert('หมดเวลาทำข้อสอบแล้ว! ระบบจะทำการส่งข้อสอบและคำนวณคะแนนอัตโนมัติ');
        submitExam();
      }
    }
  }, 1000);
}

function updateTimerUI() {
  const m = Math.floor(state.timerSeconds / 60);
  const s = state.timerSeconds % 60;
  timerDisplay.innerText = `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
  if (state.timerSeconds < 300) {
    timerDisplay.style.color = 'var(--accent-rose)';
  } else {
    timerDisplay.style.color = 'var(--accent-amber)';
  }
}

// Render Current Question
function renderCurrentQuestion() {
  const q = state.questions[state.currentIndex];
  if (!q) return;

  // Badges
  qSectionBadge.innerText = q.sectionName;
  qTopicBadge.innerText = q.topic || (state.currentSubject === 'math' ? 'คณิตศาสตร์ ป.6' : (state.currentSubject === 'thai' ? 'ภาษาไทย ป.6' : 'วิทยาศาสตร์ ป.6'));
  qDiffBadge.innerText = `ความยาก: ${q.difficulty}`;
  qLoBadge.innerText = q.learningObjective || 'LO-Gen';
  qPointsBadge.innerText = `${q.points} คะแนน`;

  // Bookmark Button State
  if (state.bookmarks.has(q.id)) {
    bookmarkBtn.classList.add('active');
    bookmarkBtn.innerHTML = '<i class="fa-solid fa-bookmark"></i>';
  } else {
    bookmarkBtn.classList.remove('active');
    bookmarkBtn.innerHTML = '<i class="fa-regular fa-bookmark"></i>';
  }

  // Scenario
  if (q.scenario) {
    scenarioContainer.style.display = 'block';
    scenarioText.innerText = q.scenario;
  } else {
    scenarioContainer.style.display = 'none';
  }

  // Question Prompt
  qNumberDisplay.innerText = `ข้อที่ ${q.id} (จาก ${state.questions.length})`;
  qTextDisplay.innerText = q.question;

  // Render Answers based on Section
  answerContainer.innerHTML = '';
  const currentAnswer = state.userAnswers[q.id];

  if (q.section === 'MCQ') {
    // 4 Options (ก, ข, ค, ง)
    const letters = ['ก', 'ข', 'ค', 'ง'];
    letters.forEach(letter => {
      const optText = q.options[letter] || '';
      const card = document.createElement('div');
      card.className = 'option-card';
      if (currentAnswer === letter) {
        card.classList.add('selected');
      }

      // After submission, show correct/wrong highlight
      if (state.isSubmitted && currentAnswer) {
        if (letter === q.correctAnswer) {
          card.classList.add('correct-highlight');
        } else if (currentAnswer === letter && letter !== q.correctAnswer) {
          card.classList.add('wrong-highlight');
        }
      }

      card.innerHTML = `
        <div class="option-letter">${letter}</div>
        <div class="option-label">${optText}</div>
      `;

      card.addEventListener('click', () => {
        if (state.isSubmitted) return;
        state.userAnswers[q.id] = letter;
        saveState();
        renderCurrentQuestion();
        renderQuestionGrid();
        updateProgressUI();
      });

      answerContainer.appendChild(card);
    });

  } else if (q.section === 'TF') {
    // True / False
    const tfGrid = document.createElement('div');
    tfGrid.className = 'tf-buttons-grid';

    const btnTrue = document.createElement('div');
    btnTrue.className = 'tf-card';
    btnTrue.innerHTML = '<i class="fa-solid fa-check"></i> จริง (True)';
    if (currentAnswer === 'True') btnTrue.classList.add('selected-true');

    const btnFalse = document.createElement('div');
    btnFalse.className = 'tf-card';
    btnFalse.innerHTML = '<i class="fa-solid fa-xmark"></i> เท็จ (False)';
    if (currentAnswer === 'False') btnFalse.classList.add('selected-false');

    if (state.isSubmitted && currentAnswer) {
      if (q.correctAnswer === 'True') {
        btnTrue.classList.add('correct-highlight');
      } else {
        btnFalse.classList.add('correct-highlight');
      }
    }

    btnTrue.addEventListener('click', () => {
      if (state.isSubmitted) return;
      state.userAnswers[q.id] = 'True';
      saveState();
      renderCurrentQuestion();
      renderQuestionGrid();
      updateProgressUI();
    });

    btnFalse.addEventListener('click', () => {
      if (state.isSubmitted) return;
      state.userAnswers[q.id] = 'False';
      saveState();
      renderCurrentQuestion();
      renderQuestionGrid();
      updateProgressUI();
    });

    tfGrid.appendChild(btnTrue);
    tfGrid.appendChild(btnFalse);
    answerContainer.appendChild(tfGrid);

  } else if (q.section === 'Scenario' || q.section === 'ShortAnswer') {
    // Textarea for descriptive answer
    const saWrapper = document.createElement('div');
    saWrapper.className = 'short-answer-zone';

    const ta = document.createElement('textarea');
    ta.className = 'sa-textarea';
    ta.placeholder = q.section === 'Scenario' 
      ? 'พิมพ์คำตอบ วิธีการคำนวณ หรือเหตุผลเชิงประยุกต์...' 
      : 'พิมพ์คำอธิบายแสดงวิธีคิด หลักการ และตัวอย่างประกอบอย่างละเอียด...';
    ta.value = currentAnswer || '';

    ta.addEventListener('input', (e) => {
      if (state.isSubmitted) return;
      state.userAnswers[q.id] = e.target.value;
      saveState();
      renderQuestionGrid();
      updateProgressUI();
    });

    const hint = document.createElement('div');
    hint.className = 'sa-hint';
    hint.innerHTML = '<i class="fa-solid fa-keyboard"></i> พิมพ์คำตอบของท่าน ระบบจะทำการบันทึกอัตโนมัติ';

    saWrapper.appendChild(ta);
    saWrapper.appendChild(hint);
    answerContainer.appendChild(saWrapper);
  }

  // Explanation Box after submitted
  if (state.isSubmitted) {
    explanationBox.style.display = 'block';
    if (q.section === 'MCQ' || q.section === 'TF') {
      const correctTxt = q.section === 'MCQ' ? `ตัวเลือก: ${q.correctAnswer}` : (q.correctAnswer === 'True' ? 'จริง (True)' : 'เท็จ (False)');
      expCorrectAnswer.innerHTML = `<strong>เฉลยที่ถูกต้อง:</strong> ${correctTxt}`;
    } else {
      expCorrectAnswer.innerHTML = `<strong>แนวคำตอบและเกณฑ์ประเมิน:</strong>`;
    }
    expText.innerText = q.explanation || q.correctAnswer;
  } else {
    explanationBox.style.display = 'none';
  }

  // Footer Navigation State
  prevBtn.disabled = (state.currentIndex === 0);
  if (state.currentIndex === state.questions.length - 1) {
    nextBtn.innerHTML = '<i class="fa-solid fa-flag-checkered"></i> ตรวจคำตอบ / ส่งข้อสอบ';
  } else {
    nextBtn.innerHTML = 'ข้อถัดไป <i class="fa-solid fa-arrow-right"></i>';
  }

  highlightCurrentGridCell();
}

// Progress Bar & Stats
function updateProgressUI() {
  const answered = Object.keys(state.userAnswers).filter(k => {
    const val = state.userAnswers[k];
    return val !== undefined && val !== null && val !== '';
  }).length;
  answeredCount.innerText = answered;
  const total = state.questions.length || 115;
  const pct = (answered / total) * 100;
  overallProgressBar.style.width = `${pct}%`;
}

// Render 115 Question Map Grid
function renderQuestionGrid() {
  questionGrid.innerHTML = '';

  state.questions.forEach((q, idx) => {
    // Filter
    if (state.activeSectionFilter !== 'ALL' && q.section !== state.activeSectionFilter) {
      return;
    }

    const hasAnswered = state.userAnswers[q.id] !== undefined && state.userAnswers[q.id] !== '';
    const isBookmarked = state.bookmarks.has(q.id);

    if (state.paletteFilter === 'unanswered' && hasAnswered) return;
    if (state.paletteFilter === 'bookmarked' && !isBookmarked) return;

    const cell = document.createElement('div');
    cell.className = 'grid-cell';
    cell.innerText = q.id;

    if (hasAnswered) cell.classList.add('answered');
    if (idx === state.currentIndex) cell.classList.add('active-current');
    if (isBookmarked) cell.classList.add('bookmarked');

    cell.addEventListener('click', () => {
      state.currentIndex = idx;
      saveState();
      renderCurrentQuestion();
    });

    questionGrid.appendChild(cell);
  });
}

function highlightCurrentGridCell() {
  const cells = questionGrid.querySelectorAll('.grid-cell');
  cells.forEach(c => {
    if (parseInt(c.innerText, 10) === state.questions[state.currentIndex]?.id) {
      c.classList.add('active-current');
    } else {
      c.classList.remove('active-current');
    }
  });
}

// Setup Event Listeners (ensure single attachment)
let listenersSetup = false;
function setupEventListeners() {
  if (listenersSetup) return;
  listenersSetup = true;

  // Subject Switcher Events
  if (subSciBtn) {
    subSciBtn.addEventListener('click', () => switchSubject('science'));
  }
  if (subMathBtn) {
    subMathBtn.addEventListener('click', () => switchSubject('math'));
  }
  if (subThaiBtn) {
    subThaiBtn.addEventListener('click', () => switchSubject('thai'));
  }
  if (subProgBtn) {
    subProgBtn.addEventListener('click', () => switchSubject('programming'));
  }
  if (subChineseBtn) {
    subChineseBtn.addEventListener('click', () => switchSubject('chinese'));
  }
  if (subEngBtn) {
    subEngBtn.addEventListener('click', () => switchSubject('english'));
  }

  // Navigation Buttons
  prevBtn.addEventListener('click', () => {
    if (state.currentIndex > 0) {
      state.currentIndex--;
      saveState();
      renderCurrentQuestion();
    }
  });

  nextBtn.addEventListener('click', () => {
    if (state.currentIndex < state.questions.length - 1) {
      state.currentIndex++;
      saveState();
      renderCurrentQuestion();
    } else {
      if (confirm('คุณมาถึงข้อสุดท้ายแล้ว ต้องการส่งข้อสอบและดูผลการประเมินหรือไม่?')) {
        submitExam();
      }
    }
  });

  // Bookmark Toggle
  bookmarkBtn.addEventListener('click', () => {
    const q = state.questions[state.currentIndex];
    if (!q) return;
    if (state.bookmarks.has(q.id)) {
      state.bookmarks.delete(q.id);
    } else {
      state.bookmarks.add(q.id);
    }
    saveState();
    renderCurrentQuestion();
    renderQuestionGrid();
  });


  // Section Filter Tabs
  const sectionTabs = document.querySelectorAll('.tab-btn');
  sectionTabs.forEach(tab => {
    tab.addEventListener('click', () => {
      sectionTabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');
      state.activeSectionFilter = tab.dataset.section;

      // Jump to first question of this section
      if (state.activeSectionFilter !== 'ALL') {
        const firstIdx = state.questions.findIndex(q => q.section === state.activeSectionFilter);
        if (firstIdx !== -1) state.currentIndex = firstIdx;
      }
      saveState();
      renderQuestionGrid();
      renderCurrentQuestion();
    });
  });

  // Palette Filter Chips
  const filterChips = document.querySelectorAll('.filter-chip');
  filterChips.forEach(chip => {
    chip.addEventListener('click', () => {
      filterChips.forEach(c => c.classList.remove('active'));
      chip.classList.add('active');
      state.paletteFilter = chip.dataset.filter;
      renderQuestionGrid();
    });
  });

  toggleTimerBtn.addEventListener('click', () => {
    state.timerPaused = !state.timerPaused;
    toggleTimerBtn.innerHTML = state.timerPaused 
      ? '<i class="fa-solid fa-play"></i>' 
      : '<i class="fa-solid fa-pause"></i>';
    toggleTimerBtn.title = state.timerPaused ? 'เริ่มจับเวลาต่อ' : 'หยุดจับเวลาชั่วคราว';
  });

  // Edit Timer (Custom Remaining Time)
  editTimerBtn.addEventListener('click', () => {
    const currentMins = Math.floor(state.timerSeconds / 60);
    const input = prompt('กำหนดเวลาคงเหลือ (นาที):', currentMins);
    if (input !== null) {
      const mins = parseInt(input, 10);
      if (!isNaN(mins) && mins >= 0) {
        state.timerSeconds = mins * 60;
        saveState();
        
        // Update display immediately
        const m = Math.floor(state.timerSeconds / 60);
        const s = state.timerSeconds % 60;
        timerDisplay.innerText = `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
      } else {
        alert('กรุณากรอกตัวเลขที่ถูกต้อง');
      }
    }
  });

  // Finish / Submit Exam Button
  finishExamBtn.addEventListener('click', () => {
    const answered = Object.keys(state.userAnswers).length;
    const remaining = state.questions.length - answered;
    const msg = remaining > 0 
      ? `คุณยังทำข้อสอบไม่ครบ (เหลืออีก ${remaining} ข้อ)\nคุณแน่ใจหรือไม่ว่าต้องการส่งข้อสอบตอนนี้?`
      : 'คุณตอบครบทุกข้อแล้ว ต้องการส่งข้อสอบและดูผลการประเมินหรือไม่?';
    if (confirm(msg)) {
      submitExam();
    }
  });

  // Reset Session
  resetSessionBtn.addEventListener('click', () => {
    if (confirm('คุณแน่ใจหรือไม่ว่าต้องการล้างคำตอบและเวลาทั้งหมดของวิชานี้เพื่อเริ่มใหม่?')) {
      const { STORAGE_KEY, RESULT_KEY } = getStorageKeys();
      localStorage.removeItem(STORAGE_KEY);
      localStorage.removeItem(RESULT_KEY);
      state.userAnswers = {};
      state.bookmarks.clear();
      state.currentIndex = 0;
      state.timerSeconds = 3600;
      state.timeSpentSeconds = 0;
      state.timerPaused = false;
      state.isSubmitted = false;
      startTimer();
      renderQuestionGrid();
      renderCurrentQuestion();
      updateProgressUI();
    }
  });

  // Study Guide Modal
  summaryNotesBtn.addEventListener('click', () => {
    summaryModal.style.display = 'flex';
  });
  closeSummaryModal.addEventListener('click', () => {
    summaryModal.style.display = 'none';
  });

  // Result Modal
  closeResultModal.addEventListener('click', () => {
    resultModal.style.display = 'none';
  });

  reviewAllAnswersBtn.addEventListener('click', () => {
    resultModal.style.display = 'none';
    renderCurrentQuestion();
  });

  retryExamBtn.addEventListener('click', () => {
    resultModal.style.display = 'none';
    const { STORAGE_KEY, RESULT_KEY } = getStorageKeys();
    localStorage.removeItem(STORAGE_KEY);
    localStorage.removeItem(RESULT_KEY);
    state.userAnswers = {};
    state.bookmarks.clear();
    state.currentIndex = 0;
    state.timerSeconds = 3600;
    state.timeSpentSeconds = 0;
    state.timerPaused = false;
    state.isSubmitted = false;
    startTimer();
    renderQuestionGrid();
    renderCurrentQuestion();
    updateProgressUI();
  });
}

// Exam Submission & Grading
function submitExam() {
  state.isSubmitted = true;
  clearInterval(state.timerInterval);

  let totalScore = 0;
  let secAScore = 0; // max 60
  let secBScore = 0; // max 30
  let secCScore = 0; // max 30
  let secDScore = 0; // max 30

  state.questions.forEach(q => {
    const userAns = state.userAnswers[q.id];
    if (!userAns) return;

    if (q.section === 'MCQ') {
      if (userAns.trim().toUpperCase() === q.correctAnswer.trim().toUpperCase()) {
        totalScore += q.points;
        secAScore += q.points;
      }
    } else if (q.section === 'TF') {
      if (userAns.trim().toLowerCase() === q.correctAnswer.trim().toLowerCase()) {
        totalScore += q.points;
        secBScore += q.points;
      }
    } else if (q.section === 'Scenario') {
      // Scenario-based text evaluation heuristic
      if (userAns.trim().length > 15) {
        totalScore += q.points;
        secCScore += q.points;
      } else if (userAns.trim().length > 0) {
        totalScore += 1;
        secCScore += 1;
      }
    } else if (q.section === 'ShortAnswer') {
      // Short answer text evaluation heuristic
      if (userAns.trim().length > 20) {
        totalScore += q.points;
        secDScore += q.points;
      } else if (userAns.trim().length > 0) {
        totalScore += 1;
        secDScore += 1;
      }
    }
  });

  // Calculate percentages
  const maxScore = state.meta.totalScore || 150;
  const pct = ((totalScore / maxScore) * 100).toFixed(1);
  const isPassed = totalScore >= state.meta.passingScore;

  // Display Scorecard
  document.getElementById('resTotalScore').innerText = totalScore;
  const statusEl = document.getElementById('resPassStatus');
  if (isPassed) {
    statusEl.className = 'status-pass';
    statusEl.innerHTML = '<i class="fa-solid fa-circle-check"></i> ยินดีด้วย! ผ่านเกณฑ์ระดับยอดเยี่ยม';
  } else {
    statusEl.className = 'status-fail';
    statusEl.innerHTML = '<i class="fa-solid fa-triangle-exclamation"></i> ยังไม่ผ่านเกณฑ์ 80% (ควรทบทวนเพิ่มเติม)';
  }

  document.getElementById('resPercentage').innerText = `คิดเป็น ${pct}% (เกณฑ์ผ่าน 80% = ${state.meta.passingScore} คะแนน)`;

  const mins = Math.floor(state.timeSpentSeconds / 60);
  const secs = state.timeSpentSeconds % 60;
  document.getElementById('resTimeSpent').innerHTML = `<i class="fa-regular fa-clock"></i> ใช้เวลาทำข้อสอบ: ${mins} นาที ${secs} วินาที`;

  // Breakdown Bars
  document.getElementById('scoreSecA').innerText = `${secAScore}/60`;
  document.getElementById('pctSecA').innerText = `${Math.round((secAScore/60)*100)}%`;
  document.getElementById('barSecA').style.width = `${(secAScore/60)*100}%`;

  document.getElementById('scoreSecB').innerText = `${secBScore}/30`;
  document.getElementById('pctSecB').innerText = `${Math.round((secBScore/30)*100)}%`;
  document.getElementById('barSecB').style.width = `${(secBScore/30)*100}%`;

  document.getElementById('scoreSecC').innerText = `${secCScore}/30`;
  document.getElementById('pctSecC').innerText = `${Math.round((secCScore/30)*100)}%`;
  document.getElementById('barSecC').style.width = `${(secCScore/30)*100}%`;

  document.getElementById('scoreSecD').innerText = `${secDScore}/30`;
  document.getElementById('pctSecD').innerText = `${Math.round((secDScore/30)*100)}%`;
  document.getElementById('barSecD').style.width = `${(secDScore/30)*100}%`;

  resultModal.style.display = 'flex';

  // Persist graded result so it survives a server reset or page reload
  saveResult({ totalScore, secAScore, secBScore, secCScore, secDScore,
               isPassed, timeSpentSeconds: state.timeSpentSeconds });
  saveState(); // Also persist the final answers
}

// Run on page load
document.addEventListener('DOMContentLoaded', init);

// Save session when user closes or navigates away from the tab
window.addEventListener('beforeunload', () => {
  saveState();
});

// Save session when user switches tabs (mobile-friendly)
document.addEventListener('visibilitychange', () => {
  if (document.visibilityState === 'hidden') {
    saveState();
  }
});
