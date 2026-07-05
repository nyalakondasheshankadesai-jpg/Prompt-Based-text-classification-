import os
import pandas as pd


class ReportGenerator:

    @staticmethod
    def generate(results, output_folder="outputs"):

        df = pd.DataFrame(results)

        html = f"""
        <!DOCTYPE html>
        <html>

        <head>

            <title>Prompt Engineering Report</title>

            <style>

            body {{
                font-family: Arial;
                margin:40px;
                background:#f5f5f5;
            }}

            h1 {{
                color:#003366;
            }}

            h2 {{
                color:#444;
            }}

            table {{
                border-collapse: collapse;
                width:100%;
                background:white;
            }}

            th, td {{
                border:1px solid #ccc;
                padding:10px;
                text-align:center;
            }}

            th {{
                background:#003366;
                color:white;
            }}

            img {{
                width:600px;
                margin-top:20px;
                border:1px solid #ddd;
                background:white;
                padding:10px;
            }}

            .section{{
                margin-top:40px;
            }}

            </style>

        </head>

        <body>

        <h1>Prompt-Based Text Classification Report</h1>

        <p>
        This report summarizes the performance of different Prompt Engineering
        strategies using Google Gemini.
        </p>

        <div class="section">

        <h2>Evaluation Metrics</h2>

        {df.to_html(index=False)}

        </div>

        <div class="section">

        <h2>Strategy Comparison</h2>

        <img src="strategy_comparison.png">

        </div>

        """

        for strategy in df["Strategy"]:

            html += f"""

            <div class="section">

            <h2>{strategy}</h2>

            <img src="{strategy}_cm.png">

            </div>

            """

        html += """

        </body>

        </html>

        """

        with open(
            os.path.join(output_folder, "report.html"),
            "w",
            encoding="utf-8"
        ) as f:

            f.write(html)

        print("HTML report generated successfully.")