$(document).ready(function () {
    function b(k) {
        var l = "";
        for (var j = 0; j < k.length; j++) {
            l = $('<div class="article" ><a><figure><a class="item_view_atlas" id="' + k[j].id + '"><img class="lazy" src="' + k[j].imgsrc + '"></a><figcaption><p class="uk-text-left item_title">' + k[j].title + '</p></figcaption></figure></a><p class="uk-text-right item_update_date"><i class="uk-badge uk-badge-black uk-icon-calendar">&nbsp;' + k[j].date + "</i></p></div>");
            a.append(l).masonry("appended", l)
        }
        $(".article").find("figcaption").addClass("uk-overlay-panel uk-overlay-bottom uk-overlay-slide-bottom uk-overlay-background");
        $(".article").find("figure").addClass("uk-overlay uk-overlay-hover");
        a.imagesLoaded().progress(function () {
            a.masonry("layout")
        });
        $("img.lazy").one("error", function (i) {
            $(this).attr("src", "static/images/404.jpg")
        })
    }

    function e(i, j, k) {
        $.ajax({
            url: "/get_item_list",
            type: "POST",
            dataType: "json",
            data: {"item_type": i, "page_num": j, "limt": k},
            error: function () {
                UIkit.notify({
                    message: '<i class="uk-icon-refresh uk-icon-spin"></i>&nbsp;第' + j + "页图册请求出错",
                    status: "info",
                    timeout: 5000,
                    pos: "top-right"
                })
            },
            beforeSend: function () {
                UIkit.notify({
                    message: '<i class="uk-icon-refresh uk-icon-spin"></i>&nbsp;正在获取第' + j + "页图册信息",
                    status: "info",
                    timeout: 5000,
                    pos: "top-right"
                })
            },
            success: function (l) {
                b(l.data);
                d == true;
                $(".item_view_atlas").off("click").click(function () {
                    if (f.has($(this).attr("id")) == true) {
                        g(f.get($(this).attr("id")))
                    } else {
                        h($(this).attr("id"))
                    }
                    window.console.log(f)
                })
            },
        })
    }

    function h(i) {
        $.ajax({
            url: "/get_items_pics", type: "POST", dataType: "json", data: {"item_id": i}, error: function () {
                UIkit.notify({
                    message: '<i class="uk-icon-refresh uk-icon-spin"></i>&nbsp;请求出错',
                    status: "info",
                    timeout: 5000,
                    pos: "top-right"
                })
            }, beforeSend: function () {
                UIkit.notify({
                    message: '<i class="uk-icon-refresh uk-icon-spin"></i>&nbsp;正在获取图册内照片',
                    status: "info",
                    timeout: 2000,
                    pos: "top-right"
                })
            }, success: function (j) {
                g(j);
                f.set(i, j);
                localStorage.setItem("pics_map", JSON.stringify(Array.from(f)))
            },
        })
    }

    function g(i) {
        var j = UIkit.lightbox.create(i);
        j.show()
    }

    if (!localStorage.getItem("pics_map")) {
        var f = new Map()
    } else {
        var f = new Map(JSON.parse(localStorage.getItem("pics_map")))
    }
    var c = 1;
    var d = true;
    var a = $("#container").masonry({itemSelector: ".article", columnWidth: 60, transitionDuration: 0, fitWidth: true});
    e($(".active_item").text(), c, 25);
    $(".items_type").off("click").click(function () {
        c = 1;
        $("#container").empty();
        $(".active_item").removeClass("active_item");
        $(this).addClass("active_item");
        e($(".active_item").text(), c, 25)
    });
    $(window).scroll(function () {
        if (d == true) {
            d == false;
            if ($(document).height() - $(this).scrollTop() - $(this).height() <= 0) {
                c++;
                $(this).scrollTop($(this).scrollTop() - 400);
                e($(".active_item").text(), c, 25)
            }
        }
    })
});