document.addEventListener('DOMContentLoaded', function() {
    const tableOrder = document.getElementById('table-order');
    const availablePool = document.getElementById('available-pool');
    const orderInput = document.getElementById('final-order-input');
    const submitBtn = document.getElementById('submit-btn');

    window.maxPlayers = 10;

    // Инициализируем Sortable только для верхней зоны (Очередь)
    Sortable.create(tableOrder, {
        animation: 150,
        ghostClass: 'sortable-ghost',
        onEnd: updateState // Обновляем скрытое поле после каждого перетаскивания
    });

    // Логика перемещения между пулом и столом
    document.addEventListener('click', function(e) {
        if (e.target.classList.contains('player-card')) {
            const card = e.target;
            const isAtTable = card.parentElement.id === 'table-order';

            if (isAtTable) {
                // Возвращаем в пул
                availablePool.appendChild(card);
            } else {
                // Добавляем за стол, если есть место
                if (tableOrder.children.length < window.maxPlayers) {
                    tableOrder.appendChild(card);
                }
            }
            updateState();
        }
    });

    window.setLimit = function(num) {
        window.maxPlayers = num;
        document.querySelectorAll('.limit-btn').forEach(b => b.classList.remove('active'));
        event.target.classList.add('active');

        // Лишних выкидываем обратно в пул
        while (tableOrder.children.length > num) {
            availablePool.appendChild(tableOrder.lastElementChild);
        }
        updateState();
    };

    function updateState() {
        const order = Array.from(tableOrder.children).map(c => c.getAttribute('data-id'));
        orderInput.value = JSON.stringify(order);

        const diff = window.maxPlayers - order.length;
        submitBtn.disabled = (diff !== 0);
        submitBtn.innerText = diff === 0 ? "Начать игру" : `Нужно выбрать ещё ${diff}`;
    }
});