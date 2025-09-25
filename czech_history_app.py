from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="Czech Republic History",
    description="A simple FastAPI app displaying the history of the Czech Republic",
    version="1.0.0"
)

@app.get("/", response_class=HTMLResponse)
async def get_czech_history():
    """
    Display the history of the Czech Republic in one paragraph
    """
    history_text = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Czech Republic History</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
                background-color: #f5f5f5;
                line-height: 1.6;
            }
            .container {
                background-color: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }
            h1 {
                color: #2c5aa0;
                text-align: center;
                margin-bottom: 30px;
                border-bottom: 3px solid #2c5aa0;
                padding-bottom: 10px;
            }
            .history-text {
                font-size: 16px;
                text-align: justify;
                color: #333;
                background-color: #f9f9f9;
                padding: 20px;
                border-left: 4px solid #2c5aa0;
                border-radius: 5px;
            }
            .flag {
                text-align: center;
                margin: 20px 0;
                font-size: 24px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>History of the Czech Republic</h1>
            <div class="flag">🇨🇿</div>
            <div class="history-text">
                The Czech Republic, located in Central Europe, has a rich and complex history that spans over a millennium. 
                The region was first settled by Celtic tribes before becoming part of the Great Moravian Empire in the 9th century. 
                The Kingdom of Bohemia emerged in the 10th century under the Přemyslid dynasty and became one of the most powerful 
                states in Central Europe, particularly during the reign of Charles IV (1346-1378), who made Prague the capital of 
                the Holy Roman Empire. The Hussite Wars in the 15th century marked a period of religious reform and national identity 
                formation, while the 17th century brought the Thirty Years' War and Habsburg domination. The 19th century saw the 
                Czech National Revival, leading to the creation of Czechoslovakia in 1918 following World War I. After Nazi occupation 
                during World War II and communist rule from 1948-1989, the peaceful Velvet Revolution brought democracy, and in 1993, 
                the Czech Republic peacefully separated from Slovakia, becoming an independent nation that joined the European Union in 2004.
            </div>
        </div>
    </body>
    </html>
    """
    return history_text

@app.get("/api/history")
async def get_czech_history_api():
    """
    API endpoint returning Czech Republic history as JSON
    """
    return {
        "country": "Czech Republic",
        "flag": "🇨🇿",
        "history": "The Czech Republic, located in Central Europe, has a rich and complex history that spans over a millennium. The region was first settled by Celtic tribes before becoming part of the Great Moravian Empire in the 9th century. The Kingdom of Bohemia emerged in the 10th century under the Přemyslid dynasty and became one of the most powerful states in Central Europe, particularly during the reign of Charles IV (1346-1378), who made Prague the capital of the Holy Roman Empire. The Hussite Wars in the 15th century marked a period of religious reform and national identity formation, while the 17th century brought the Thirty Years' War and Habsburg domination. The 19th century saw the Czech National Revival, leading to the creation of Czechoslovakia in 1918 following World War I. After Nazi occupation during World War II and communist rule from 1948-1989, the peaceful Velvet Revolution brought democracy, and in 1993, the Czech Republic peacefully separated from Slovakia, becoming an independent nation that joined the European Union in 2004."
    }

@app.get("/health")
async def health_check():
    """
    Health check endpoint
    """
    return {"status": "healthy", "message": "Czech Republic History API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
