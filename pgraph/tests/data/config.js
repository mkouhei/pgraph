$(function(){

    var load_linkdraw = function(pkg_name, version, task_id, loading_msg) {
        if (task_id == null) {
            var url = "/api/linkdraw/" + pkg_name + "/" + version;
        } else {
            var url = "/api/linkdraw/" + pkg_name + "/" + version + "?task=" + task_id;
        }
        $.getJSON(url, function(json) {
            switch(json.status) {
            case 200:
                console.log("drawing lindraw.")
                draw(pkg_name, url);
                break;
            case 202:
                show_msg(loading_msg, "warning");
                console.log(json.descr);
                setTimeout(function(name, version, task_id) {
                    loading_msg = loading_msg + ".";
                    load_linkdraw(name, version, task_id, loading_msg);
                }, 3000, pkg_name, version, json.task);
                break;
            case 404:
                console.log(json.descr);
                show_msg(json.descr, "danger");
                break;
            default:
                console.log('error: not handling case.');
                break;
            }
        });
    }

    function show_msg(msg, alert_level) {
        var alert_class = "alert alert-dismissible";
        if (alert_level == "warning") {
            alert_class = "alert alert-warning";
        } else if (alert_level == "danger") {
            alert_class = "alert alert-danger";
        }
        $("#message").css("text-align", "center");
        $("#message strong")
            .attr("class", alert_class)
            .text(msg)
            .css("font-size", "xx-large");
    }

    function draw(pkg_name, url) {
        $("#message")
            .removeAttr("class")
            .text("");
        $("#graph").linkDraw({
            "configPath": url,
            "positionPath": "positions/" + pkg_name + ".json",
            "positionWriter": "api/positions",
            "positionSave": false,
            //"zoom": false,
            //"drag": false,
            "width": 800,
            "height": 600,
            "interval":0
        });
    };

    var loading_msg = "loading.";
    load_linkdraw("py-deps", "0.2.0", null, loading_msg);
});
