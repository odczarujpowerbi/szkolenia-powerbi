```js
    function drag(event) {
        event.dataTransfer.setData('function', event.target.getAttribute('data-function'));
    }

    function allowDrop(event) {
        event.preventDefault();
        event.target.classList.add('drag-over');
    }

    function dragLeave(event) {
        event.target.classList.remove('drag-over');
    }

    function drop(event) {
        event.preventDefault();
        event.target.classList.remove('drag-over');

        const functionName = event.dataTransfer.getData('function');
        const slotIndex = parseInt(event.target.getAttribute('data-slot'));

        const activePage = document.querySelector('.page.active');
        if (!activePage) return;

        if (slots[slotIndex]) {
            const chips = activePage.querySelectorAll('.function-chip');
            for (let i = 0; i < chips.length; i++) {
                if (chips[i].getAttribute('data-function') === slots[slotIndex]) {
                    chips[i].classList.remove('used');
                    break;
                }
            }
        }

        slots[slotIndex] = functionName;
        event.target.textContent = functionName;

        // Resetuj WSZYSTKIE luki do szarego koloru (soft reset)
        const zones = activePage.querySelectorAll('.drop-zone');
        for (let i = 0; i < zones.length; i++) {
            zones[i].classList.remove('correct', 'incorrect');
            if (zones[i].textContent) {
                zones[i].classList.add('filled');
            }
        }

        const chips = activePage.querySelectorAll('.function-chip');
        for (let i = 0; i < chips.length; i++) {
            if (chips[i].getAttribute('data-function') === functionName) {
                chips[i].classList.add('used');
                break;
            }
        }

        const feedback = activePage.querySelector('.feedback');
        if (feedback) {
            feedback.classList.remove('show');
        }
    }

    function checkSolution() {
        const activePage = document.querySelector('.page.active');
        if (!activePage) return;

        const feedback = activePage.querySelector('.feedback');
        if (!feedback) return;

        if (slots.includes('')) {
            feedback.className = 'feedback show incorrect';
            feedback.innerHTML = 'Niekompletne! Musisz wypełnić wszystkie miejsca w kodzie.';
            return;
        }

        const currentPageNum = parseInt(activePage.getAttribute('data-page'));
        const pageIndex = currentPageNum - 1;

        // Zwiększ liczbę prób
        taskAttempts[pageIndex]++;

        const isCorrect = checkCurrentPageSolution(pageIndex);
        const zones = activePage.querySelectorAll('.drop-zone');

        if (isCorrect) {
            feedback.className = 'feedback show correct';
            feedback.innerHTML = correctFeedback[pageIndex];

            // Pokoloruj luki na zielono
            for (let i = 0; i < zones.length; i++) {
                zones[i].classList.remove('filled', 'incorrect');
                zones[i].classList.add('correct');
            }

            // Oznacz jako poprawnie wykonane (tylko za pierwszym razem)
            if (!taskCompleted[pageIndex]) {
                taskCompleted[pageIndex] = true;
                taskCorrect[pageIndex] = true;
            }
        } else {
            const userAnswer = slots.join(',');
            const incorrectMessages = incorrectFeedback[pageIndex];

            // Pokoloruj luki - zielone dla poprawnych, czerwone dla błędnych
            const solution = correctSolutions[pageIndex];
            for (let i = 0; i < zones.length; i++) {
                zones[i].classList.remove('filled');
                if (slots[i] === solution[i]) {
                    zones[i].classList.add('correct');
                } else {
                    zones[i].classList.add('incorrect');
                }
            }

            for (const pattern in incorrectMessages) {
                if (pattern === userAnswer) {
                    feedback.className = 'feedback show incorrect';
                    feedback.innerHTML = incorrectMessages[pattern];

                    // Oznacz jako zakończone (nawet jeśli błędnie)
                    if (!taskCompleted[pageIndex]) {
                        taskCompleted[pageIndex] = true;
                        taskCorrect[pageIndex] = false;
                    }
                    return;
                }

                if (pattern.includes('*')) {
                    const regexPattern = '^' + pattern.replace(/\*/g, '.*') + '$';
                    const regex = new RegExp(regexPattern);
                    if (regex.test(userAnswer)) {
                        feedback.className = 'feedback show incorrect';
                        feedback.innerHTML = incorrectMessages[pattern];

                        // Oznacz jako zakończone (nawet jeśli błędnie)
                        if (!taskCompleted[pageIndex]) {
                            taskCompleted[pageIndex] = true;
                            taskCorrect[pageIndex] = false;
                        }
                        return;
                    }
                }
            }

            const defaultMessage = incorrectMessages['default'];
            feedback.className = 'feedback show incorrect';
            feedback.innerHTML = defaultMessage || '❌ <strong>Niepoprawne rozwiązanie.</strong> Spróbuj ponownie!';

            // Oznacz jako zakończone (nawet jeśli błędnie)
            if (!taskCompleted[pageIndex]) {
                taskCompleted[pageIndex] = true;
                taskCorrect[pageIndex] = false;
            }
        }
    }

    function checkCurrentPageSolution(pageIndex) {
        const solution = correctSolutions[pageIndex];
        for (let i = 0; i < solution.length; i++) {
            if (slots[i] !== solution[i]) {
                return false;
            }
        }
        return true;
    }

    function resetTask() {
        slots.fill('');

        const activePage = document.querySelector('.page.active');
        if (!activePage) return;

        const zones = activePage.querySelectorAll('.drop-zone');
        for (let i = 0; i < zones.length; i++) {
            zones[i].textContent = '';
            zones[i].classList.remove('filled', 'correct', 'incorrect');
        }

        const chips = activePage.querySelectorAll('.function-chip');
        for (let i = 0; i < chips.length; i++) {
            chips[i].classList.remove('used');
        }

        const feedback = activePage.querySelector('.feedback');
        if (feedback) {
            feedback.classList.remove('show');
        }
    }

    function showPage(pageNumber) {
        const pages = document.querySelectorAll('.page');
        for (let i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }

        for (let i = 0; i < pages.length; i++) {
            if (parseInt(pages[i].getAttribute('data-page')) === pageNumber) {
                pages[i].classList.add('active');
                break;
            }
        }

        currentPage = pageNumber;

        // Jeśli to strona podsumowania
        if (currentPage === totalPages) {
            updateSummary();
            document.getElementById('currentPage').textContent = 'Podsumowanie';
        } else {
            const pageIndex = currentPage - 1;
            document.getElementById('currentPage').textContent = currentPage;
            slots = new Array(slotsPerPage[pageIndex]).fill('');
            resetTask();
        }

        // Zmień przycisk "Następne" na "Zakończ" przed ostatnim zadaniem
        const nextBtn = document.getElementById('nextBtn');
        if (currentPage === totalTasks) {
            nextBtn.textContent = 'Zakończ →';
        } else if (currentPage < totalPages) {
            nextBtn.textContent = 'Następne →';
        }

        document.getElementById('prevBtn').disabled = (currentPage === 1);
        document.getElementById('nextBtn').disabled = (currentPage === totalPages);
    }

    function updateSummary() {
        // Oblicz statystyki
        let completedCount = 0;
        let correctCount = 0;

        for (let i = 0; i < totalTasks; i++) {
            if (taskCompleted[i]) {
                completedCount++;
                if (taskCorrect[i]) {
                    correctCount++;
                }
            }
        }

        const percentage = completedCount > 0 ? Math.round((correctCount / completedCount) * 100) : 0;

        // Aktualizuj główne statystyki
        document.getElementById('completedCount').textContent = completedCount;
        document.getElementById('percentageScore').textContent = percentage;

        // Generuj szczegóły zadań
        let summaryHTML = '';
        for (let i = 0; i < totalTasks; i++) {
            const status = !taskCompleted[i] ? 'skipped' : (taskCorrect[i] ? 'correct' : 'incorrect');
            const statusText = !taskCompleted[i] ? '⚪ Pominięte' : (taskCorrect[i] ? '✅ Poprawnie' : '❌ Niepoprawnie');
            const attemptsText = taskAttempts[i] > 0 ? ` (Próby: ${taskAttempts[i]})` : '';

            summaryHTML += `
                <div class='task-summary-item ${status}'>
                    <strong>Zadanie ${i + 1}:</strong> ${statusText}${attemptsText}
                </div>
            `;
        }

        document.getElementById('tasksSummary').innerHTML = summaryHTML;
    }

    function resetAllTasks() {
        // Reset wszystkich statystyk
        for (let i = 0; i < totalTasks; i++) {
            taskAttempts[i] = 0;
            taskCompleted[i] = false;
            taskCorrect[i] = false;
        }

        // Reset wszystkich stron zadań
        const pages = document.querySelectorAll('.page');
        for (let i = 0; i < totalTasks; i++) {
            const page = pages[i];
            if (!page) continue;

            const zones = page.querySelectorAll('.drop-zone');
            for (let j = 0; j < zones.length; j++) {
                zones[j].textContent = '';
                zones[j].classList.remove('filled', 'correct', 'incorrect');
            }

            const chips = page.querySelectorAll('.function-chip');
            for (let j = 0; j < chips.length; j++) {
                chips[j].classList.remove('used');
            }

            const feedback = page.querySelector('.feedback');
            if (feedback) {
                feedback.classList.remove('show');
            }
        }

        // Wróć do pierwszego zadania
        showPage(1);
    }

    function nextPage() {
        if (currentPage < totalPages) {
            showPage(currentPage + 1);
        }
    }

    function prevPage() {
        if (currentPage > 1) {
            showPage(currentPage - 1);
        }
    }

    document.addEventListener('DOMContentLoaded', function() {
        showPage(1);
    });
```
