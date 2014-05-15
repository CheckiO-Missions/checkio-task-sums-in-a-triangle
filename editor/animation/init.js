//Dont change it
requirejs(['ext_editor_1', 'jquery_190', 'raphael_210'],
    function (ext, $, TableComponent) {

        var cur_slide = {};

        ext.set_start_game(function (this_e) {
        });

        ext.set_process_in(function (this_e, data) {
            cur_slide["in"] = data[0];
        });

        ext.set_process_out(function (this_e, data) {
            cur_slide["out"] = data[0];
        });

        ext.set_process_ext(function (this_e, data) {
            cur_slide.ext = data;
            this_e.addAnimationSlide(cur_slide);
            cur_slide = {};
        });

        ext.set_process_err(function (this_e, data) {
            cur_slide['error'] = data[0];
            this_e.addAnimationSlide(cur_slide);
            cur_slide = {};
        });

        ext.set_animate_success_slide(function (this_e, options) {
            var $h = $(this_e.setHtmlSlide('<div class="animation-success"><div></div></div>'));
            this_e.setAnimationHeight(115);
        });

        ext.set_animate_slide(function (this_e, data, options) {
            var $content = $(this_e.setHtmlSlide(ext.get_template('animation'))).find('.animation-content');
            if (!data) {
                console.log("data is undefined");
                return false;
            }

            var checkioInput = data.in;
            var checkioInputStr = JSON.stringify(checkioInput).replace(/\[/g, "(").replace(/\]/g, ")").replace(/\((\d)\)/, "(\$1,)");

            if (data.error) {
                $content.find('.call').html('Fail: count_gold(' + checkioInputStr + ')');
                $content.find('.output').html(data.error.replace(/\n/g, ","));

                $content.find('.output').addClass('error');
                $content.find('.call').addClass('error');
                $content.find('.answer').remove();
                $content.find('.explanation').remove();
                this_e.setAnimationHeight($content.height() + 60);
                return false;
            }

            var rightResult = data.ext["answer"];
            var userResult = data.out;
            var result = data.ext["result"];
            var result_addon = data.ext["result_addon"];


            //if you need additional info from tests (if exists)
            var explanation = data.ext["explanation"];

            $content.find('.output').html('&nbsp;Your result:&nbsp;' + JSON.stringify(userResult));

            if (!result) {
                $content.find('.call').html('Fail: count_gold(' + checkioInputStr + ')');
                $content.find('.answer').html('Right result:&nbsp;' + JSON.stringify(rightResult));
                $content.find('.answer').addClass('error');
                $content.find('.output').addClass('error');
                $content.find('.call').addClass('error');
            }
            else {
                $content.find('.call').html('Pass: count_gold(' + checkioInputStr + ')');
                $content.find('.answer').remove();
            }
            //Dont change the code before it
            console.log(explanation);
            if (explanation) {
                var canvas = new SumInTriangleCanvas(checkioInput, explanation);
                canvas.createCanvas($content.find(".explanation")[0]);
            }
            else {
                $content.find('.explanation').remove();
            }


            this_e.setAnimationHeight($content.height() + 60);

        });

        function SumInTriangleCanvas(dataInput, dataExplanation){
            var zx = 10;
            var zy = 10;
            var cellSize = 30;
            var cellN = dataInput.length;
            var fullSizeX = zx * 2 + cellSize * cellN;
            var fullSizeY = zy * 2 + cellSize * cellN;

            var colorDark = "#294270";
            var colorOrange = "#FABA00";
            var colorBlue = "#8FC7ED";
            var colorWhite = "#FFFFFF";

            var attrRect = {"stroke": colorDark, "stroke-width": 1, "fill": colorBlue};
            var attrRectPath = {"stroke": colorDark, "stroke-width": 1, "fill": colorOrange};
            var attrText = {"stroke": colorDark, "font-size": 16, "font-family": "Verdana"};

            var paper;

            this.createCanvas = function(dom) {
                paper = Raphael(dom, fullSizeX, fullSizeY, 0, 0);
                for (var i = 0; i < cellN; i++) {
                    for (var j = 0; j <= i; j++){
                        paper.rect(
                            fullSizeX / 2 - (i+1) * cellSize / 2 + j * cellSize,
                            zy + cellSize * i,
                        cellSize, cellSize).attr(
                               j == dataExplanation[i]? attrRectPath: attrRect);
                        paper.text(
                            fullSizeX / 2 - i * cellSize / 2 + j * cellSize,
                            zy + cellSize * i + cellSize / 2,
                            String(dataInput[i][j])).attr(attrText);

                    }
                }

            }

        }


    }
);
