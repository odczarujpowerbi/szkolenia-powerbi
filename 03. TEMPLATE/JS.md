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
})();
</script>

```
  

