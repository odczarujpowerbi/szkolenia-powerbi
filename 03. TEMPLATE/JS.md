```js
<script>
(function() {
    // Unikalny ID dla tej wizualizacji (wstrzykiwany przez Python)
    var vizId = '{{UNIQUE_ID}}';
    var containerId = 'viz_' + vizId;

    var currentPage_{{UNIQUE_ID}} = 1;
    var container = document.getElementById(containerId);

    if (!container) return;

    var pages = container.querySelectorAll('.page');
    var totalPages = pages.length;

    document.getElementById('totalPages_' + vizId).textContent = totalPages;

    window['showPage_{{UNIQUE_ID}}'] = function(n) {
        if (n > totalPages) currentPage_{{UNIQUE_ID}} = totalPages;
        if (n < 1) currentPage_{{UNIQUE_ID}} = 1;

        for (var i = 0; i < pages.length; i++) {
            pages[i].classList.remove('active');
        }
        pages[currentPage_{{UNIQUE_ID}} - 1].classList.add('active');

        document.getElementById('currentPage_' + vizId).textContent = currentPage_{{UNIQUE_ID}};
        document.getElementById('prevBtn_' + vizId).disabled = (currentPage_{{UNIQUE_ID}} === 1);
        document.getElementById('nextBtn_' + vizId).disabled = (currentPage_{{UNIQUE_ID}} === totalPages);
    };

    window['changePage_{{UNIQUE_ID}}'] = function(n) {
        currentPage_{{UNIQUE_ID}} += n;
        window['showPage_{{UNIQUE_ID}}'](currentPage_{{UNIQUE_ID}});
    };

    // Inicjalizacja
    window['showPage_{{UNIQUE_ID}}'](1);

    // Funkcjonalność powiększania obrazów
    var images = container.querySelectorAll('img');
    images.forEach(function(img) {
        img.style.cursor = 'pointer';
        img.style.transition = 'transform 0.3s ease';

        img.addEventListener('click', function() {
            if (this.classList.contains('zoomed')) {
                // Pomniejsz obraz
                this.classList.remove('zoomed');
                this.style.position = '';
                this.style.top = '';
                this.style.left = '';
                this.style.transform = '';
                this.style.width = '100%';
                this.style.maxWidth = '';
                this.style.maxHeight = '';
                this.style.zIndex = '';
                this.style.backgroundColor = '';
                this.style.padding = '';
                this.style.boxShadow = '';
            } else {
                // Powiększ obraz
                this.classList.add('zoomed');
                this.style.position = 'fixed';
                this.style.top = '50%';
                this.style.left = '50%';
                this.style.transform = 'translate(-50%, -50%)';
                this.style.width = 'auto';
                this.style.maxWidth = '95vw';
                this.style.maxHeight = '95vh';
                this.style.zIndex = '9999';
                this.style.backgroundColor = 'rgba(255, 255, 255, 0.95)';
                this.style.padding = '10px';
                this.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.3)';
            }
        });
    });
})();
</script>

```
  

