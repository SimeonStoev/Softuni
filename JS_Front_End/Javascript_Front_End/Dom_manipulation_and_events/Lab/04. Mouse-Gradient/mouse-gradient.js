function attachGradientEvents() {
    //TODO
    const divEl = document.getElementById('gradient');

    divEl.addEventListener('mousemove', calcPercenage);
    divEl.addEventListener('mouseout', returnDefault);

    function calcPercenage(e) {
        const { offsetX, target } = e;
        const { clientWidth } = target;
        const percent = Math.floor((offsetX / clientWidth) * 100);
        document.getElementById("result").textContent = `${percent}%`;
    }

    function returnDefault(e) {
        document.getElementById("result").textContent = '';
    }
}
