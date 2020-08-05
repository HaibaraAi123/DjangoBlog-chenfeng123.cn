/*!
 * JavaScript for Blog of FengChan (https://chenfeng123.cn)
 * Copyright 2019-2020 chenfeng123.cn
 * Licensed under the Creative Commons Attribution 3.0 Unported License. For
 * details, see https://creativecommons.org/licenses/by/3.0/.
 */
 !
function(a){
    "use strict";
    a(function(){
        var b = a(window),
        c = a(document.body);
        /*使用scrollspy滚动监听.bs-sidebar*/
        c.scrollspy({
            target:".sidebar"
        }),
        b.on("load",
            function(){
                c.scrollspy("refresh")
        }),
        a('.bs-docs-container [href="#"]').click(function(a){
            a.preventDefault()
        }),
        /*bootstrap3 affix控件 实现侧边栏位置不动 在bootstrap4 中不可用*/
        setTimeout(function(){
            var b = a(".sidebar");
            b.affix({
                offset:{
                    top:0,
                    bottom: function(){
                        return this.bottom = a(".footer").outerHeight(!0)
                    }
                }
            })
        },
        100),
        /*bootstrap3 模态框实现复用 用于/album 照片详细展示*/
        a("#modal_photo").on("show.bs.modal",
        function(b) {
            var trigger = a(b.relatedTarget),
            photo_src = trigger.data('src'),
            photo_describle = trigger.data('describle'),
            modal = a(this);

            modal.find('.modal-body p').text(photo_describle);
            modal.find('.modal-body img').attr('src', photo_src);
        }),
        a(document).ready(function(){
            a(document).off("click.bs.dropdown.data-api");
            var b = a(".dropdown-toggle");
            c = a(".dropdown")

            b.mouseover(function(){
                c.addClass('open');
            });
            c.mouseover(function(){
                c.addClass('open')
            }).mouseout(function(){
                c.removeClass('open');
            })

        })
    })
}(jQuery);