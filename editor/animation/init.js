//Don't change it
requirejs(['ext_editor_io2', 'jquery_190', 'raphael_210'],
    function (extIO, $, rr) {
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

            var attrRect = {"stroke": colorDark, "stroke-width": 1, "fill": colorBlue};
            var attrRectPath = {"stroke": colorDark, "stroke-width": 1, "fill": colorOrange};
            var attrText = {"stroke": colorDark, "font-size": 16, "font-family": "Verdana"};

            var paper;

            this.createCanvas = function(dom) {
                paper = Raphael(dom, fullSizeX, fullSizeY, 0, 0);
                for (var i = 0; i < cellN; i++) {
                    for (var j = 0; j <= i; j++) {
                        paper.rect(fullSizeX / 2 - (i + 1) * cellSize / 2 + j * cellSize, zy + cellSize * i, cellSize, cellSize, 5)
                            .attr(j == dataExplanation[i] ? attrRectPath : attrRect);
                        paper.text(fullSizeX / 2 - i * cellSize / 2 + j * cellSize,
                            zy + cellSize * i + cellSize / 2, String(dataInput[i][j]))
                            .attr(attrText)
                    }
                }
            }
        };
        var io = new extIO({
            animation: function ($expl, data) {
                var canvas = new SumInTriangleCanvas(data.in[0], data.ext.explanation);
                canvas.createCanvas($expl[0])
            }
        });
        io.start()
    }
);
