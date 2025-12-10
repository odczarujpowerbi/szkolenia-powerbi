```js
    document.getElementById('totalPages').textContent = totalPages;

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
            feedback.textContent = 'Proszę najpierw wybrać odpowiedź!';
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
```
