```css
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            font-size: 16px;
            font-weight: 400;
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
            background: #6b1718;
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
            background: #380c0c;
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
            font-size: 26px;
            line-height: 36px;
            font-weight: 600;
            padding-top: 14px;
            padding-bottom: 6px;
            margin-bottom: 1em;
            color: #6b1718;
            border-bottom: 2px solid #6b1718;
        }

        h2 {
            font-size: 26px;
            line-height: 36px;
            font-weight: 600;
            padding-top: 14px;
            padding-bottom: 6px;
            margin: 1.5em 0 0.8em 0;
            color: #1a1a1a;
            border-bottom: 2px solid #1a1a1a;
        }

        .question-box {
            background: #f8f9fa;
            border-left: 3px solid #6b1718;
            padding: 20px;
            margin: 1.5em 0;
            border-radius: 3px;
        }

        .question-box p {
            margin: 0;
            font-size: 1.05em;
            color: #1a1a1a;
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
            border-color: #6b1718;
            background: #fef5f5;
        }

        .answer-option.selected {
            border-color: #6b1718;
            background: #ffe5e6;
        }

        .answer-option.correct {
            border-color: #ccc;
            background: #d4edda;
        }

        .answer-option.incorrect {
            border-color: #b82b4e;
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
            border-left: 3px solid #b82b4e;
            color: #721c24;
        }

        .check-button {
            margin-top: 1.5em;
            background: #121212;
        }

        .check-button:hover:not(:disabled) {
            background: #111111;
        }

        .check-button:disabled {
            background: #ccc;
        }

        pre {
            background: #f8f9fa;
            border-left: 3px solid #6b1718;
            padding: 18px;
            margin: 1em 0;
            overflow-x: auto;
            border-radius: 3px;
        }

        code {
            font-family: 'Fira Code', 'Courier New', monospace;
            font-size: 0.95em;
            color: #b82b4e;
        }

        .score-box {
            background: #6b1718;
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
            border-left-color: #b82b4e;
        }

        strong {
            font-weight: 700;
            color: #1a1a1a;
        }

        p {
            margin-bottom: 1em;
        }
```
