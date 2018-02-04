function onSend() {
    var value = $("#recipient").val();
    var name = $("#stafflist [value='" + value + "']").attr('data-value');
    var msg = $("#messagebox").val();
    console.log(value);
    console.log(name);
    if (name == undefined) {
        alert("Name not found");
        return;
    }
    $.getJSON("/sendmsg",{
        message: msg,
        username: name
    })
}