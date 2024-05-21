// File: static/script.js
document.getElementById('predict-form').addEventListener('submit', async function(event) {
    event.preventDefault();

    const data = {
        'Year': parseFloat(document.getElementById('year').value),
        'Country of Headquarters': document.getElementById('country').value,
        'Standard Industry Classification Code': parseFloat(document.getElementById('industry_code').value),
        'Fiscal Year-end Month': parseFloat(document.getElementById('fiscal_year_end').value),
        'Long-Term Debt - Total': parseFloat(document.getElementById('long_term_debt').value),
        'Revenue - Total': parseFloat(document.getElementById('revenue').value),
        'Stockholders Equity - Total': parseFloat(document.getElementById('equity').value),
        'Com Shares Outstanding - Issue': parseFloat(document.getElementById('shares_outstanding').value),
        'Net Income (Loss) - Consolidated': parseFloat(document.getElementById('net_income').value),
        'price - close monthly': parseFloat(document.getElementById('price_close').value),
        'currency': document.getElementById('currency').value,
    };

    const response = await fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ features: Object.values(data) }),
    });

    const result = await response.json();
    document.getElementById('result').innerText = 'Prediction: ' + result.prediction;
});
