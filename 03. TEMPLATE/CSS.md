```css
  <style>
        * {
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
        
        h2 {
            font-size: 1.4em;
            font-weight: 600;
            margin: 1.5em 0 0.8em 0;
            color: #2a2a2a;
        }
        
        h3 {
            font-size: 1.1em;
            font-weight: 600;
            margin: 1.2em 0 0.6em 0;
            color: #444;
        }
        
        p {
            margin-bottom: 1em;
            font-size: 1.05em;
        }
        
        strong {
            font-weight: 600;
            color: #1a1a1a;
        }
        
        code {
            background: #f5f5f5;
            padding: 3px 7px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            font-size: 0.95em;
            color: #d73a49;
        }
        
        pre {
            background: #f8f9fa;
            border-left: 3px solid #0066cc;
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
            color: #0066cc;
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
            margin: 1em 0 1em 1.5em;
        }
        
        li {
            margin: 0.5em 0;
            font-size: 1.05em;
        }
        
        .iteration-box {
            border-left: 3px solid #0066cc;
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
