$(document).ready(function () {


    //chapter2 选择元素

    //添加、删除样式
    $('#tips').addClass('bg-gray');
    $('#tips').removeClass('');

    /**
     * :eq()选择符、 :odd和:even选择符都使用JavaScript内置从0开始的编号方式，因此，第一行的编号为0（偶数），第二行的编号为1（奇数） ，依此类推
     */
    // $('tr:even').addClass('alt');
    /**
     * 这个选择符相对于元素的父元素而非当前选择的所有元素来计算位置，它可以接受数值、 odd或even作为参数
     * :nth-child()是jQuery中唯一从1开始计数的选择符
     */
    $('tr:nth-child(odd)').addClass('alt');

    //$('tr:contains(Henry)').addClass('highlight'); //区分大小写 henry


    /**
     * $('input[type="radio"]:checked')
     */

    /**
     * 遍历，效果同上
     */
    // $('tr').filter(':even').addClass('alt');

    /**
     * .next()方法只选择下一个最接近的同辈元素。要想突出显示Henry所在单元格后面的全部
     单元格，可以使用.nextAll()方法
     有读者可能已经猜到了， .next()和.nextAll()方法分别有一个对应方法，即.prev()
     和.prevAll()。此外， .siblings()能够选择处于相同DOM层次的所有其他元素，无论这些
     元素处于当前元素之前还是之后
     */
    //$('td:contains(Henry)').next().addClass('highlight'); //下一项
    //$('td:contains(Henry)').nextAll().addBack().addClass('highlight');

    //$('td:contains(Henry)').parent().children().addClass('highlight');

    $('td:contains(Henry)') //取得包含Henry的所有单元格
        .parent() //取得它的父元素
        .find('td:eq(1)') //在父元素中查找第2个单元格
        .addClass('highlight') //为该单元格添加hightlight类
        .end() //恢复到包含Henry的单元格的父元素
        .find('td:eq(2)') //在父元素中查找第3个单元格
        .addClass('highlight'); //为该单元格添加hightlight类

    /**
     * 所有选择符表达式和多数jQuery方法都返回一个jQuery对象，而这通常都是我们所希望的，
     * 因为jQuery对象能够提供隐式迭代和连缀能力。
     * 尽管如此，我们仍然有可能需要在代码中直接访问DOM元素。
     */
    var myTag = $('#my-element').get(0).tagName;
    var myTag = $('#my-element')[0].tagName;
    console.log("#my-element tag name = " + myTag);
});