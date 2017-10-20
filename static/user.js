function takeScreenShot(username) {
    html2canvas(document.getElementById("timetable"), {
        onrendered: function (canvas) {
            var width = $('#timetable').width();
            var height = $('#timetable').height();
            var tempcanvas=document.createElement('canvas');
            tempcanvas.width=width; //this controls picture size
            tempcanvas.height=height;
            var context=tempcanvas.getContext('2d');
            context.drawImage(canvas,0,0,width,height,0,0,width,height);
            var link=document.createElement("a");
            link.href=tempcanvas.toDataURL('image/jpg');
            link.download = username.concat('-timetable.jpg');
            link.click();
        }
    });
};
