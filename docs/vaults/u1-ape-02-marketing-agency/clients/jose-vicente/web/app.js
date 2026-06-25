document.addEventListener('DOMContentLoaded', () => {
    // 1. Elementos del Simulador de Viabilidad BDE
    const amountInput = document.getElementById('project-amount');
    const rateInput = document.getElementById('subsidy-rate');
    
    const amountDisplay = document.getElementById('amount-val');
    const rateDisplay = document.getElementById('rate-val');
    
    const resCredito = document.getElementById('res-credito');
    const resSubsidio = document.getElementById('res-subsidio');
    const resViabilidad = document.getElementById('res-viabilidad');

    function calcularViabilidad() {
        const monto = parseFloat(amountInput.value);
        const tasa = parseFloat(rateInput.value);

        // Actualizardisplays visuales
        amountDisplay.textContent = `$${monto.toLocaleString('en-US')}`;
        rateDisplay.textContent = `${tasa}%`;

        // Algoritmo de Viabilidad Financiera BDE
        const subsidio = monto * (tasa / 100);
        const credito = monto - subsidio;
        
        let viabilidad = "MEDIA";
        if (tasa >= 60) {
            viabilidad = "EXCEPCIONAL";
            resViabilidad.className = "result-number font-green";
        } else if (tasa >= 40) {
            viabilidad = "ALTA";
            resViabilidad.className = "result-number font-green";
        } else {
            viabilidad = "MODERADA";
            resViabilidad.className = "result-number";
            resViabilidad.style.color = "#F59E0B"; // Color Ámbar
        }

        // Renderizarresultados
        resCredito.textContent = `$${credito.toLocaleString('en-US')}`;
        resSubsidio.textContent = `$${subsidio.toLocaleString('en-US')}`;
        resViabilidad.textContent = viabilidad;
    }

    // Escuchar sliders
    amountInput.addEventListener('input', calcularViabilidad);
    rateInput.addEventListener('input', calcularViabilidad);

    // Inicializar
    calcularViabilidad();


    // 2. Formulario de Captura de Leads del Curso
    const courseForm = document.getElementById('course-form');
    const successBox = document.getElementById('success-message');

    courseForm.addEventListener('submit', (e) => {
        e.preventDefault();

        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const whatsapp = document.getElementById('whatsapp').value;
        const sector = document.getElementById('sector').value;

        const leadData = {
            name,
            business: `Curso JV - Sector: ${sector}`,
            whatsapp,
            niche: "gastronomia", // Mapeado a nicho genérico del backend
            message: `Email: ${email} | Pre-inscrito al curso de José Vicente`
        };

        const btnSubmit = document.getElementById('btn-submit');
        btnSubmit.textContent = 'Procesando registro...';
        btnSubmit.disabled = true;

        // POST a la API backend local
        fetch('/api/leads', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(leadData)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Backend desconectado');
            }
            return response.json();
        })
        .then(data => {
            console.log('[API Cliente] Registro exitoso al curso:', data);
            mostrarExito();
        })
        .catch(err => {
            console.warn('[API Cliente] Guardando lead en fallback local:', err);
            
            leadData.timestamp = new Date().toISOString();
            let leads = JSON.parse(localStorage.getItem('jv_course_leads') || '[]');
            leads.push(leadData);
            localStorage.setItem('jv_course_leads', JSON.stringify(leads));
            
            mostrarExito();
        });
    });

    function mostrarExito() {
        courseForm.classList.add('hidden');
        successBox.classList.remove('hidden');
        document.getElementById('registro').scrollIntoView({ behavior: 'smooth' });
    }
});
