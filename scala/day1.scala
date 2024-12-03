//> using scala 3.5.2
//> using toolkit default

def readInput(): Seq[String] =
    val path: os.Path = os.pwd / "inputs" / "day1.txt"
    val lines: Seq[String] = os.read.lines(path)
    lines

def part1(lines: Seq[String], delimiter: String) =
    val firstSet: Seq[Int] = lines.map(
        x => x.split(delimiter)(0).toInt
    ).sorted
    val secondSet: Seq[Int] = lines.map(
        x => x.split(delimiter)(1).toInt
    ).sorted
    val difference = (firstSet zip secondSet).map{
        case (x, y) => (x - y).abs
    }.foldLeft(0)(_+_)

    println(difference)

def part2(lines: Seq[String], delimiter: String) = 

    val firstSet: Seq[Int] = lines.map(
        x => x.split(delimiter)(0).toInt
    )
    val secondSet: Seq[Int] = lines.map(
        x => x.split(delimiter)(1).toInt
    )

    val similarity = firstSet.map(
        x => secondSet.filter(_ == x).length * x
    ).foldLeft(0)(_+_)

    println(similarity)

@main def day1() =
    val lines: Seq[String] = readInput()
    val delimiter = "   "
    part1(lines, delimiter)
    part2(lines, delimiter)