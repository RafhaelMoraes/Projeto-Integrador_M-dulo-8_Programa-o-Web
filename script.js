document.getElementById('surveyForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Impede o comportamento padrão do formulário

    // Coleta os dados do formulário
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const rating = document.getElementById('rating').value;
    const comments = document.getElementById('comments').value;

    // Envia os dados para o servidor
    fetch('/submit_survey', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name, email, rating, comments })
    })
    .then(response => response.json())
    .then(data => {
        // Exibe a mensagem de sucesso
        document.getElementById('response').textContent = data.message;
        document.getElementById('response').style.color = 'green';
    })
    .catch(error => {
        console.error('Erro:', error);
        document.getElementById('response').textContent = 'Erro ao enviar feedback.';
        document.getElementById('response').style.color = 'red';
    });
});