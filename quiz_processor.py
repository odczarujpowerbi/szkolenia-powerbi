"""Quiz processor module for handling quiz markdown parsing and HTML generation.

This module provides functionality to parse quiz content from markdown format
and generate interactive HTML quiz interfaces. It supports quiz metadata extraction,
answer validation, and user feedback mechanisms.

Functions:
    parse_quiz_markdown: Parses quiz markdown content into structured data
    create_quiz_html: Generates interactive HTML quiz from parsed question data
"""

from text_utils import format_user_text


def create_quiz_html(title, questions, css='', js=''):
    """Tworzy interaktywny quiz w formacie HTML

    Args:
        title: str - tytuł quizu
        questions: list[dict] - lista pytań z odpowiedziami
            [{'question': str, 'answers': [str], 'correct': int, 'explanation': str}]
        css: str - opcjonalny zewnętrzny CSS (jeśli pusty, używa wbudowanych stylów)
        js: str - opcjonalny zewnętrzny JS (jeśli pusty, używa wbudowanego)

    Returns:
        str: kompletny HTML z quizem (gotowy do osadzenia w miarze Power BI)
    """
    use_inline_styles = not css  # Jeśli nie ma zewnętrznego CSS, użyj wbudowanego
    total_questions = len(questions)
    total_pages = total_questions + 1  # pytania + strona podsumowania

    html_parts = []

    # DOCTYPE i HTML header
    html_parts.append("<!DOCTYPE html>\n")
    html_parts.append("<html lang='pl'>\n")
    html_parts.append("<head>\n")
    html_parts.append("    <meta charset='UTF-8'>\n")
    html_parts.append("    <meta name='viewport' content='width=device-width, initial-scale=1.0'>\n")
    html_parts.append(f"    <title>{title}</title>\n")

    # CSS - zewnętrzny z konfiguracji lub wbudowany
    if css:
        # Użyj zewnętrznego CSS z szablonu
        html_parts.append("    <style>\n")
        for line in css.split('\n'):
            html_parts.append(f"    {line}\n")
        html_parts.append("    </style>\n")
    elif use_inline_styles:
        # Użyj wbudowanych stylów (inline)
        html_parts.append("    <style>\n")
        html_parts.append("""        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            font-size: 16px;
            line-height: 1.7;
            color: #333;
            background: transparent;
            padding: 20px;
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
            background: transparent;
            padding: 40px;
        }

        .navigation {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 40px;
            padding-bottom: 20px;
            border-bottom: 1px solid #e1e4e8;
        }

        button {
            background: #0066cc;
            color: white;
            border: none;
            padding: 12px 28px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 1em;
            font-weight: 500;
            transition: background 0.2s;
        }

        button:hover {
            background: #0052a3;
        }

        button:disabled {
            background: #ccc;
            cursor: not-allowed;
        }

        .page-indicator {
            color: #666;
            font-size: 1em;
        }

        .page {
            display: none;
            min-height: 500px;
        }

        .page.active {
            display: block;
            animation: fadeIn 0.3s ease-in;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        h1 {
            font-size: 1.8em;
            font-weight: 600;
            margin-bottom: 1em;
            color: #1a1a1a;
        }

        .question-box {
            background: #f8f9fa;
            border-left: 3px solid #0066cc;
            padding: 20px;
            margin: 1.5em 0;
            border-radius: 3px;
        }

        .answers {
            margin-top: 1.5em;
        }

        .answer-option {
            background: white;
            border: 2px solid #e1e4e8;
            padding: 15px 20px;
            margin: 10px 0;
            border-radius: 4px;
            cursor: pointer;
            transition: all 0.2s;
            font-size: 1.05em;
        }

        .answer-option:hover {
            border-color: #0066cc;
            background: #f0f7ff;
        }

        .answer-option.selected {
            border-color: #0066cc;
            background: #e6f2ff;
        }

        .answer-option.correct {
            border-color: #28a745;
            background: #d4edda;
        }

        .answer-option.incorrect {
            border-color: #dc3545;
            background: #f8d7da;
        }

        .feedback {
            margin-top: 1.5em;
            padding: 15px 20px;
            border-radius: 4px;
            display: none;
            font-size: 1.05em;
        }

        .feedback.show {
            display: block;
        }

        .feedback.correct {
            background: #d4edda;
            border-left: 3px solid #28a745;
            color: #155724;
        }

        .feedback.incorrect {
            background: #f8d7da;
            border-left: 3px solid #dc3545;
            color: #721c24;
        }

        .check-button {
            margin-top: 1.5em;
            background: #28a745;
        }

        .check-button:hover:not(:disabled) {
            background: #218838;
        }

        .check-button:disabled {
            background: #ccc;
        }

        pre {
            background: #f8f9fa;
            border-left: 3px solid #0066cc;
            padding: 18px;
            margin: 1em 0;
            overflow-x: auto;
            border-radius: 3px;
        }

        code {
            font-family: 'Courier New', monospace;
            font-size: 0.95em;
        }

        .score-box {
            background: #0066cc;
            color: white;
            padding: 20px;
            border-radius: 4px;
            text-align: center;
            font-size: 1.2em;
            margin-bottom: 2em;
        }

        .summary-item {
            background: #f8f9fa;
            padding: 15px;
            margin: 10px 0;
            border-radius: 4px;
            border-left: 3px solid #ccc;
        }

        .summary-item.correct {
            border-left-color: #28a745;
        }

        .summary-item.incorrect {
            border-left-color: #dc3545;
        }
""")
        html_parts.append("    </style>\n")

    html_parts.append("</head>\n")
    html_parts.append("<body>\n\n")

    # Container i nawigacja
    html_parts.append("<div class='container'>\n")
    html_parts.append("    <!-- Nawigacja na górze -->\n")
    html_parts.append("    <div class='navigation'>\n")
    html_parts.append("        <button id='prevBtn' onclick='changePage(-1)'>← Poprzednia</button>\n")
    html_parts.append("        <span class='page-indicator'>\n")
    html_parts.append("            Pytanie <span id='currentPage'>1</span> z <span id='totalPages'>")
    html_parts.append(str(total_pages))
    html_parts.append("</span>\n")
    html_parts.append("        </span>\n")
    html_parts.append("        <button id='nextBtn' onclick='changePage(1)'>Następna →</button>\n")
    html_parts.append("    </div>\n\n")

    # Generuj strony z pytaniami
    for idx, q in enumerate(questions):
        page_class = "page active" if idx == 0 else "page"
        html_parts.append(f"    <!-- Pytanie {idx + 1} -->\n")
        html_parts.append(f"    <div class='{page_class}'>\n")
        html_parts.append(f"        <h1>Pytanie {idx + 1}</h1>\n")
        html_parts.append("        <div class='question-box'>\n")
        html_parts.append(f"            <p><strong>{format_user_text(q['question'], 'html')}</strong></p>\n")
        html_parts.append("        </div>\n")
        html_parts.append("        <div class='answers'>\n")

        # Odpowiedzi
        for ans_idx, answer in enumerate(q['answers']):
            html_parts.append(f"            <div class='answer-option' onclick='selectAnswer({idx}, {ans_idx})'>\n")
            html_parts.append(f"                {format_user_text(answer, 'html')}\n")
            html_parts.append("            </div>\n")

        html_parts.append("        </div>\n")
        html_parts.append(f"        <button class='check-button' onclick='checkAnswer({idx}, {q['correct']})'>Sprawdź odpowiedź</button>\n")
        html_parts.append(f"        <div class='feedback' id='feedback-{idx}'></div>\n")
        html_parts.append("    </div>\n\n")

    # Strona podsumowania
    html_parts.append("    <!-- Podsumowanie quizu -->\n")
    html_parts.append("    <div class='page'>\n")
    html_parts.append("        <h1>Podsumowanie quizu</h1>\n")
    html_parts.append("        <div class='score-box' id='finalScore'>\n")
    html_parts.append(f"            Twój wynik: <span id='scoreText'>0/{total_questions}</span> (<span id='percentText'>0%</span>)\n")
    html_parts.append("        </div>\n")
    html_parts.append("        <div id='summaryContent'></div>\n")
    html_parts.append("        <button onclick='restartQuiz()' style='margin-top: 20px; width: 100%;'> Rozpocznij quiz od nowa</button>\n")
    html_parts.append("    </div>\n")
    html_parts.append("</div>\n\n")

    # JavaScript
    html_parts.append("<script>\n")

    # Część 1: Dynamiczne dane specyficzne dla tego quizu
    html_parts.append(f"    let currentPage = 1;\n")
    html_parts.append(f"    const totalPages = {total_pages};\n")
    html_parts.append(f"    const totalQuestions = {total_questions};\n")
    html_parts.append("    \n")
    html_parts.append(f"    const userAnswers = new Array(totalQuestions).fill(null);\n")
    html_parts.append(f"    const answeredQuestions = new Array(totalQuestions).fill(false);\n")
    html_parts.append("    \n")

    # Array z poprawnymi odpowiedziami
    correct_answers = [str(q['correct']) for q in questions]
    html_parts.append(f"    const correctAnswers = [{', '.join(correct_answers)}];\n")
    html_parts.append("    \n")

    # Array z wyjaśnieniami
    html_parts.append("    const explanations = [\n")
    for idx, q in enumerate(questions):
        # Najpierw przetworz markdown, potem escape dla DAX/innerHTML
        explanation_formatted = format_user_text(q['explanation'], 'innerHTML')
        comma = "," if idx < len(questions) - 1 else ""
        html_parts.append(f"        '{explanation_formatted}'{comma}\n")
    html_parts.append("    ];\n")
    html_parts.append("    \n")

    # Część 2: Funkcje - z template lub inline
    if js:
        # Użyj zewnętrznego JS z szablonu
        for line in js.split('\n'):
            html_parts.append(f"    {line}\n")
    else:
        # Użyj wbudowanego JS (inline)
        html_parts.append("""    document.getElementById('totalPages').textContent = totalPages;

    function selectAnswer(questionIndex, answerIndex) {
        if (answeredQuestions[questionIndex]) return;

        const answers = document.querySelectorAll('.page')[questionIndex].querySelectorAll('.answer-option');
        answers.forEach(a => a.classList.remove('selected'));
        answers[answerIndex].classList.add('selected');
        userAnswers[questionIndex] = answerIndex;
    }

    function checkAnswer(questionIndex, correctIndex) {
        if (answeredQuestions[questionIndex]) return;

        const answers = document.querySelectorAll('.page')[questionIndex].querySelectorAll('.answer-option');
        const feedback = document.getElementById('feedback-' + questionIndex);
        const checkBtn = document.querySelectorAll('.page')[questionIndex].querySelector('.check-button');

        if (userAnswers[questionIndex] === null) {
            feedback.className = 'feedback show incorrect';
            feedback.textContent = '⚠️ Proszę najpierw wybrać odpowiedź!';
            return;
        }

        answeredQuestions[questionIndex] = true;
        checkBtn.disabled = true;

        const isCorrect = userAnswers[questionIndex] === correctIndex;

        answers.forEach((answer, index) => {
            answer.style.cursor = 'default';
            if (index === correctIndex) {
                answer.classList.add('correct');
            } else if (index === userAnswers[questionIndex]) {
                answer.classList.add('incorrect');
            }
        });

        feedback.className = 'feedback show ' + (isCorrect ? 'correct' : 'incorrect');
        feedback.innerHTML = (isCorrect ? '✅ Świetnie! ' : '❌ Nieprawidłowo. ') + explanations[questionIndex];

        if (questionIndex < totalQuestions - 1) {
            setTimeout(() => {
                changePage(1);
            }, 2500);
        } else {
            setTimeout(() => {
                showSummary();
                changePage(1);
            }, 2500);
        }
    }

    function showSummary() {
        let correctCount = 0;
        for (let i = 0; i < totalQuestions; i++) {
            if (userAnswers[i] === correctAnswers[i]) {
                correctCount++;
            }
        }

        const percentage = Math.round((correctCount / totalQuestions) * 100);
        document.getElementById('scoreText').textContent = correctCount + '/' + totalQuestions;
        document.getElementById('percentText').textContent = percentage + '%';

        let summaryHTML = '<h2>Szczegóły odpowiedzi:</h2>';
        for (let i = 0; i < totalQuestions; i++) {
            const isCorrect = userAnswers[i] === correctAnswers[i];
            summaryHTML += `
                <div class='summary-item ${isCorrect ? 'correct' : 'incorrect'}'>
                    <strong>Pytanie ${i + 1}:</strong> ${isCorrect ? '✅ Poprawnie' : '❌ Niepoprawnie'}<br>
                    <small>${explanations[i]}</small>
                </div>
            `;
        }

        document.getElementById('summaryContent').innerHTML = summaryHTML;
    }

    function restartQuiz() {
        userAnswers.fill(null);
        answeredQuestions.fill(false);
        currentPage = 1;

        document.querySelectorAll('.page').forEach((page, index) => {
            if (index < totalQuestions) {
                const answers = page.querySelectorAll('.answer-option');
                answers.forEach(a => {
                    a.className = 'answer-option';
                    a.style.cursor = 'pointer';
                });
                const feedback = page.querySelector('.feedback');
                feedback.className = 'feedback';
                const checkBtn = page.querySelector('.check-button');
                checkBtn.disabled = false;
            }
        });

        showPage(1);
    }

    function showPage(n) {
        const pages = document.querySelectorAll('.page');

        if (n > totalPages) currentPage = totalPages;
        if (n < 1) currentPage = 1;

        pages.forEach(page => page.classList.remove('active'));
        pages[currentPage - 1].classList.add('active');

        document.getElementById('currentPage').textContent = currentPage;
        document.getElementById('prevBtn').disabled = currentPage === 1;
        document.getElementById('nextBtn').disabled = currentPage === totalPages;

        window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    function changePage(n) {
        currentPage += n;
        showPage(currentPage);
    }

    document.addEventListener('keydown', function(e) {
        if (e.key === 'ArrowLeft') changePage(-1);
        if (e.key === 'ArrowRight') changePage(1);
    });

    showPage(1);
""")

    html_parts.append("</script>\n\n")
    html_parts.append("</body>\n")
    html_parts.append("</html>\n")

    return ''.join(html_parts)


def parse_quiz_markdown(content):
    """Parsuje plik quizu w formacie markdown

    Format quizu:
    # Tytuł quizu

    ## Pytanie 1
    **Treść pytania**
    - A) Odpowiedź A
    - B) Odpowiedź B
    - C) Odpowiedź C
    - D) Odpowiedź D
    ---
    correct: 0
    explanation: Wyjaśnienie

    Args:
        content: str - zawartość pliku quizu (bez frontmatter)

    Returns:
        tuple: (quiz_title, questions_list)
            - quiz_title: tytuł quizu (z pierwszego # H1)
            - questions_list: lista słowników z pytaniami
              [{'question': str, 'answers': [str], 'correct': int, 'explanation': str}]
    """
    lines = content.split('\n')

    # Wyciągnij tytuł quizu (pierwszy # H1)
    quiz_title = "Quiz"
    for line in lines:
        if line.startswith('# '):
            quiz_title = line[2:].strip()
            break

    # Podziel na sekcje pytań (## Pytanie)
    questions = []
    current_question = None
    current_answers = []
    in_metadata = False
    metadata_lines = []

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # Nowe pytanie
        if line.startswith('## '):
            # Zapisz poprzednie pytanie (jeśli istnieje)
            if current_question and current_answers:
                # Parsuj metadata
                correct_idx = 0
                explanation = ""
                for meta_line in metadata_lines:
                    if meta_line.startswith('correct:'):
                        correct_idx = int(meta_line.split(':', 1)[1].strip())
                    elif meta_line.startswith('explanation:'):
                        explanation = meta_line.split(':', 1)[1].strip()

                questions.append({
                    'question': current_question,
                    'answers': current_answers,
                    'correct': correct_idx,
                    'explanation': explanation
                })

            # Reset dla nowego pytania
            current_question = None
            current_answers = []
            in_metadata = False
            metadata_lines = []
            i += 1
            continue

        # Treść pytania (bold **text**)
        if line.startswith('**') and line.endswith('**'):
            current_question = line[2:-2]
            i += 1
            continue

        # Odpowiedzi (- A), - B), etc.)
        if line.startswith('- '):
            current_answers.append(line[2:].strip())
            i += 1
            continue

        # Separator metadata (---)
        if line == '---':
            in_metadata = True
            i += 1
            continue

        # Metadata (correct, explanation)
        if in_metadata and line:
            metadata_lines.append(line)

        i += 1

    # Zapisz ostatnie pytanie
    if current_question and current_answers:
        correct_idx = 0
        explanation = ""
        for meta_line in metadata_lines:
            if meta_line.startswith('correct:'):
                correct_idx = int(meta_line.split(':', 1)[1].strip())
            elif meta_line.startswith('explanation:'):
                explanation = meta_line.split(':', 1)[1].strip()

        questions.append({
            'question': current_question,
            'answers': current_answers,
            'correct': correct_idx,
            'explanation': explanation
        })

    return quiz_title, questions
