document.addEventListener('DOMContentLoaded', () => {
    // 1. Elementos de la Calculadora de ROI
    const budgetInput = document.getElementById('budget');
    const ticketInput = document.getElementById('ticket');
    
    const budgetDisplay = document.getElementById('budget-val');
    const ticketDisplay = document.getElementById('ticket-val');
    
    const resVentas = document.getElementById('res-ventas');
    const resIngresos = document.getElementById('res-ingresos');
    const resRoas = document.getElementById('res-roas');

    // Parámetros de Simulación (Benchmarks Locales de AMDL)
    const CPC = 0.15; // Costo por Clic estimado de USD 0.15 en Loja
    const TasaConversion = 0.025; // 2.5% conservador para PYMEs

    function calcularROI() {
        const presupuesto = parseFloat(budgetInput.value);
        const ticket = parseFloat(ticketInput.value);

        // Actualizar displays visuales
        budgetDisplay.textContent = `$${presupuesto}`;
        ticketDisplay.textContent = `$${ticket}`;

        // Algoritmo Cuantitativo
        const clicsEstimados = presupuesto / CPC;
        const ventasAdicionales = Math.round(clicsEstimados * TasaConversion);
        const ingresosEstimados = ventasAdicionales * ticket;
        const roas = presupuesto > 0 ? (ingresosEstimados / presupuesto).toFixed(2) : 0;

        // Renderizar resultados con animaciones de números si es posible
        resVentas.textContent = ventasAdicionales;
        resIngresos.textContent = `$${ingresosEstimados.toLocaleString('en-US')}`;
        resRoas.textContent = `${roas}x`;

        // Ajustar color de ROAS para destacar salud financiera
        if (roas >= 3.0) {
            resRoas.className = 'result-number font-green';
        } else {
            resRoas.className = 'result-number';
            resRoas.style.color = '#F59E0B'; // Ambar/Alerta si el ROAS es bajo
        }
    }

    // Escuchar cambios interactivos en sliders
    budgetInput.addEventListener('input', calcularROI);
    ticketInput.addEventListener('input', calcularROI);

    // Inicializar cálculos
    calcularROI();


    // 2. Elementos del Formulario de Captura de Leads (Test de Humo)
    const smokeForm = document.getElementById('smoke-test-form');
    const successBox = document.getElementById('success-message');
    const successBusinessSpan = document.getElementById('success-business');

    smokeForm.addEventListener('submit', (e) => {
        e.preventDefault();

        // Extraer datos del formulario
        const name = document.getElementById('name').value;
        const business = document.getElementById('business').value;
        const whatsapp = document.getElementById('whatsapp').value;
        const niche = document.getElementById('niche').value;
        const message = document.getElementById('message').value;

        const leadData = {
            name,
            business,
            whatsapp,
            niche,
            message
        };

        // Transición visual elegante (animación de envío)
        const btnSubmit = document.getElementById('btn-submit');
        const originalText = btnSubmit.textContent;
        btnSubmit.textContent = 'Procesando registro...';
        btnSubmit.disabled = true;

        // Intentar registrar en el backend real mediante fetch
        fetch('/api/leads', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(leadData)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Servidor local desconectado o respuesta errónea');
            }
            return response.json();
        })
        .then(data => {
            console.log('[API] Registro exitoso en backend:', data);
            mostrarExito(business);
        })
        .catch(err => {
            console.warn('[API] Servidor local no disponible. Activando fallback de alta resiliencia (localStorage):', err);
            
            // Fallback: guardar en localStorage si el backend de Python no está corriendo en ese momento
            leadData.timestamp = new Date().toISOString();
            let leads = JSON.parse(localStorage.getItem('amdl_leads') || '[]');
            leads.push(leadData);
            localStorage.setItem('amdl_leads', JSON.stringify(leads));
            
            mostrarExito(business);
        });
    });

    function mostrarExito(business) {
        // Ocultar formulario de forma suave
        smokeForm.classList.add('hidden');
        
        // Cargar datos en la caja de éxito
        successBusinessSpan.textContent = business;
        
        // Mostrar la confirmación premium
        successBox.classList.remove('hidden');
        
        // Hacer scroll suave al inicio de la tarjeta de contacto
        document.getElementById('contacto').scrollIntoView({ behavior: 'smooth' });
    }
});
