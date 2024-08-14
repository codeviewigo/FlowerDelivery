// Пример скрипта для обновления корзины
document.addEventListener('DOMContentLoaded', function() {
    const cartItems = document.querySelectorAll('.form-control[type="number"]');
    
    cartItems.forEach(item => {
        item.addEventListener('change', function() {
            updateCartTotal();
        });
    });

    function updateCartTotal() {
        let total = 0;
        cartItems.forEach(item => {
            const price = parseFloat(item.closest('tr').querySelector('td:nth-child(3)').textContent.replace('$', ''));
            const quantity = item.value;
            total += price * quantity;
        });
        document.querySelector('h3').textContent = 'Итого: $' + total;
    }
});
