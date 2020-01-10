function rTime() {

    var lclock = new Date();
    var h = lclock.getHours();
    var m = lclock.getMinutes();
    var s = lclock.getSeconds();

    var ap = (h < 12) ? 'AM' : 'PM';

    h = (h > 12) ? h - 12 : h;

    h = ('0' + h).slice(-2);
    m = ('0' + m).slice(-2);
    s = ('0' + s).slice(-2);

    document.getElementById('clock').innerHTML =
    '<h1>' + h + ':' + m + ':' + s + ' ' + ap + '</h1>';

    var t = setTimeout(rTime, 500);
}
