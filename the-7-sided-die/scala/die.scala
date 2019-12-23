import scala.util.Random
import scala.collection.mutable.Map

object Die {

    val r = new Random()

    def main (args: Array[String]): Unit = {
        Benchmark.run(the6SidedDie.roll)
        Benchmark.run(the7SidedDie.rollWithPartition)
        Benchmark.run(the7SidedDie.rollWithFormula)
    }

    object the6SidedDie {

        def roll(): Int = r.nextInt(6)+1
    }

    object the7SidedDie {

        def roll(): Int = r.nextInt(7)+1

        def rollWithPartition(): Int =  (the6SidedDie.roll, the6SidedDie.roll) 
        match {
            case (6,6) => rollWithPartition()
            case (_,6) => 7
            case (n,_) => n
        }

        def rollWithFormula(): Int = {

            val fstDraw = the6SidedDie.roll
            val sndDraw = the6SidedDie.roll

            if (fstDraw == 6 && sndDraw == 6) 
                rollWithFormula
            else
                ((fstDraw-1)*6 + sndDraw) % 7 + 1
        }
    }

    object Benchmark {

        def run(f: () => Int): Unit = {

            val res : Map[Int,Int] = Map()
            val t0 = System.nanoTime
            for (i <- 1 to 10000000){
                val draw = f()
                res(draw) = (res getOrElse (draw,0)) + 1
            }
            val t1 = System.nanoTime

            for ((k,v) <- res) printf("key: %s, value: %s\n", k, v) 
            println("Roll took %f seconds.".format((t1-t0)/10E9))
        }
    }
}
