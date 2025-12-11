```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    font-size: 16px;
    line-height: 1.6;
    color: #333;
    background: transparent;
    padding: 20px;
}

.container {
    max-width: 900px;
    margin: 0 auto;
    background: transparent;
    padding: 40px;
}

h3 {
    font-size: 26px;
    line-height: 36px;
    font-weight: 600;
    padding-top: 14px;
    padding-bottom: 6px;
    margin-bottom: 1em;
    color: #6b1718;
    border-bottom: 2px solid #6b1718;
}

.task-description {
    font-size: 1.1em;
    margin: 20px 0;
}

.code-container {
    background: #f8f9fa;
    border: 2px solid #e1e4e8;
    border-radius: 6px;
    padding: 25px;
    margin: 30px 0;
    font-family: 'Courier New', monospace;
    font-size: 1.05em;
    line-height: 1.8;
}

.drop-zone {
    display: inline-block;
    min-width: 180px;
    height: 36px;
    background: white;
    border: 2px dashed #6b1718;
    border-radius: 4px;
    padding: 6px 12px;
    margin: 0 4px;
    vertical-align: middle;
    text-align: center;
    transition: all 0.2s;
}

.drop-zone.drag-over {
    background: #ffe6e6;
    border-color: #380c0c;
}

.drop-zone.filled {
    background: #d4edda;
    border: 2px solid #28a745;
    border-style: solid;
}

.functions-title {
    font-size: 1em;
    margin: 30px 0 15px 0;
    color: #333;
}

.function-chip {
    display: inline-block;
    background: #6b1718;
    color: white;
    padding: 10px 20px;
    margin: 8px;
    border-radius: 20px;
    cursor: grab;
    font-family: 'Courier New', monospace;
    font-size: 1em;
    font-weight: 500;
    transition: all 0.2s;
    user-select: none;
}

.function-chip:hover {
    background: #380c0c;
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(107, 23, 24, 0.3);
}

.function-chip:active {
    cursor: grabbing;
}

.function-chip.used {
    opacity: 0.3;
    cursor: not-allowed;
    pointer-events: none;
}

.button-group {
    margin-top: 30px;
    display: flex;
    gap: 15px;
    align-items: center;
}

button {
    background: #6b1718;
    color: white;
    border: none;
    padding: 14px 32px;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1.05em;
    font-weight: 600;
    transition: all 0.2s;
}

button:hover {
    background: #380c0c;
    transform: translateY(-1px);
}

button.reset-btn {
    background: #6b1718;
    padding: 8px 16px;
    font-size: 0.9em;
}

button.reset-btn:hover {
    background: #380c0c;
}

.feedback {
    margin-top: 25px;
    padding: 20px;
    border-radius: 6px;
    display: none;
    font-size: 1.05em;
}

.feedback.show {
    display: block;
    animation: slideDown 0.3s ease-out;
}

@keyframes slideDown {
    from {
        opacity: 0;
        transform: translateY(-10px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.feedback.correct {
    background: #d4edda;
    border-left: 4px solid #28a745;
    color: #155724;
}

.feedback.incorrect {
    background: #f8d7da;
    border-left: 4px solid #dc3545;
    color: #721c24;
}

.hint-box {
    background: #fafafa;
    border-left: 4px solid #ccc;
    padding: 15px;
    margin: 20px 0;
    border-radius: 4px;
    color: #121212;
    font-size: 0.95em;
}
.pagination {
    display: flex;
    align-items: center;
    justify-content: space-between; 
    gap: 20px;
    margin: 30px auto; 
    padding: 20px;
    border-radius: 6px;
	max-width: 900px;
    border-bottom: 1px solid #e0e0e0;
    width: 100%;
}

.page-info {
    font-weight: 600;
    color: #666666; 
}

.nav-button {
    background: #6b1718;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 4px;
    cursor: pointer;
    font-size: 1em;
    transition: all 0.2s;
}

.nav-button:hover:not(:disabled) {
    background: #380c0c;
    transform: translateY(-1px);
}

.nav-button:disabled {
    background: #ccc;
    cursor: not-allowed;
    opacity: 0.5;
}


.nav-button:disabled {
    background: #ccc;
    cursor: not-allowed;
    opacity: 0.5;
}


.page {
    display: none;
}

.page.active {
    display: block;
}
```
