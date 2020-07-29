$( document ).ready(function() {
    function createCanvas() {
        var canvas = document.getElementById("gameCanvas");
        canvas.context = canvas.getContext('2d');
        return canvas;
    }

    function component(width, height, color, x, y, canvas) {
        this.width = width;
        this.height = height;
        this.x = x;
        this.y = y;
        ctx = canvas.context;
        ctx.fillStyle = color;
        ctx.fillRect(this.x, this.y, this.width, this.height);
}
    var gameBoard = createCanvas();
    var gamePiece = new component(30, 30, "red", 10, 120, gameBoard);
});