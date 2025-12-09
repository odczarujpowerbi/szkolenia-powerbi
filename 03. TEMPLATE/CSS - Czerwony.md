```css
  <style>
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

        h3 {
            font-size: 1.1em;
            font-weight: 600;
            margin: 1.2em 0 0.6em 0;
            padding-bottom: 5px;
            color: #444;
            border-bottom: 1px solid #999;
        }

        p {
            margin-bottom: 1em;
            font-size: 1.05em;
        }

        strong {
            font-weight: 700;
            color: #1a1a1a;
        }

        code {
            background: #f5f5f5;
            padding: 3px 7px;
            border-radius: 3px;
            font-family: 'Fira Code', 'Courier New', monospace;
            font-size: 0.95em;
            color: #b82b4e;
        }

        pre {
            background: #f8f9fa;
            border-left: 3px solid #6b1718;
            padding: 18px;
            margin: 1em 0;
            overflow-x: auto;
            border-radius: 3px;
        }

        pre code {
            background: none;
            padding: 0;
            color: #24292e;
            font-size: 1em;
            line-height: 1.6;
        }

        .dax-keyword {
            color: #6b1718;
            font-weight: 600;
        }

        .dax-function {
            color: #6f42c1;
        }

        .dax-number {
            color: #005cc5;
        }

        .dax-comment {
            color: #6a737d;
            font-style: italic;
        }

        ul, ol {
            margin: 0.3em 0;
            padding-left: 1.8em;
        }

        li {
            margin: 0;
            padding-left: 0.2em;
            font-size: 1.05em;
            line-height: 1.6;
        }

        ol {
            list-style-type: decimal;
        }

        ol li::marker {
            color: #999;
            font-weight: 400;
        }

        ul li::marker {
            color: #999;
        }

        ul ul, ol ol, ul ol, ol ul {
            margin: 0.2em 0;
            padding-left: 1.5em;
        }

        blockquote {
            border-left: 3px solid #6b1718;
            background: #f8f9fa;
            padding: 14px 18px;
            margin: 1em 0;
            color: #555;
            font-style: italic;
        }

        blockquote p {
            margin: 0;
        }

        .iteration-box {
            border-left: 3px solid #6b1718;
            padding: 14px 18px;
            margin: 0.8em 0;
        }

        .result-box {
            background: #f5f5f5;
            border-left: 3px solid #999;
            padding: 14px 18px;
            margin: 0.8em 0;
            font-weight: 500;
            color: #555;
            font-size: 1.05em;
        }
    </style>

```
