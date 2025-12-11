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
        event.target.classList.add('filled');

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
        const isCorrect = checkCurrentPageSolution(pageIndex);

        if (isCorrect) {
            feedback.className = 'feedback show correct';
            feedback.innerHTML = correctFeedback[pageIndex];
        } else {
            const userAnswer = slots.join(',');
            const incorrectMessages = incorrectFeedback[pageIndex];

            for (const pattern in incorrectMessages) {
                if (pattern === userAnswer) {
                    feedback.className = 'feedback show incorrect';
                    feedback.innerHTML = incorrectMessages[pattern];
                    return;
                }

                if (pattern.includes('*')) {
                    const regexPattern = '^' + pattern.replace(/\*/g, '.*') + '$';
                    const regex = new RegExp(regexPattern);
                    if (regex.test(userAnswer)) {
                        feedback.className = 'feedback show incorrect';
                        feedback.innerHTML = incorrectMessages[pattern];
                        return;
                    }
                }
            }

            const defaultMessage = incorrectMessages['default'];
            feedback.className = 'feedback show incorrect';
            feedback.innerHTML = defaultMessage || '❌ <strong>Niepoprawne rozwiązanie.</strong> Spróbuj ponownie!';
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
            zones[i].classList.remove('filled');
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
        const pageIndex = currentPage - 1;
        document.getElementById('currentPage').textContent = currentPage;

        document.getElementById('prevBtn').disabled = (currentPage === 1);
        document.getElementById('nextBtn').disabled = (currentPage === totalPages);

        slots = new Array(slotsPerPage[pageIndex]).fill('');

        resetTask();
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
