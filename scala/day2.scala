//> using scala 3.5.2
//> using toolkit default

package day2
def readInput() =
    val path: os.Path = os.pwd / "inputs" / "day2.txt"
    val lines: Seq[String] = os.read.lines(path)
    val linesFormatted: Seq[Seq[Int]] = lines.map(
        _.split(" ").map(_.toInt)
    )
    linesFormatted

def isDecreasingAndSafe(line: Seq[Int]): Boolean =
    val result = (line.take(line.length-1) zip line.takeRight(line.length-1)).map{
        case (x, y) => (x < y && ((x - y).abs <= 3))
    }.foldLeft(true)(_ && _)
    result

def isIncreasingAndSafe(line: Seq[Int]): Boolean =
    val result = (line.take(line.length-1) zip line.takeRight(line.length-1)).map{
        case (x, y) => (x > y && ((x - y).abs <= 3))
    }.foldLeft(true)(_ && _)
    result

def isDecreasingAndSafeRemoveOne(line: Seq[Int]) =
    if isDecreasingAndSafe(line) then
        true
    else
        (0 to line.length).map(
            i => line.take(i) ++ line.takeRight(line.length - i - 1)
        ).map(isDecreasingAndSafe).foldLeft(false)(_ || _)

def isIncreasingAndSafeRemoveOne(line: Seq[Int]) =
    if isIncreasingAndSafe(line) then
        true
    else
        (0 to line.length).map(
            i => line.take(i) ++ line.takeRight(line.length - i - 1)
        ).map(isIncreasingAndSafe).foldLeft(false)(_ || _)


def part1(lines: Seq[Seq[Int]]) =
    var numSafe = 0
    for line <- lines do
        if (isIncreasingAndSafe(line) || isDecreasingAndSafe(line)) then
            numSafe += 1
    println(numSafe)

def part2(lines: Seq[Seq[Int]]) = 
    var numSafe = 0
    for line <- lines do
        if (isIncreasingAndSafeRemoveOne(line) || isDecreasingAndSafeRemoveOne(line)) then
            numSafe += 1
    println(numSafe)

@main def day2() =
    val lines: Seq[Seq[Int]] = readInput()
    part1(lines)
    part2(lines)
