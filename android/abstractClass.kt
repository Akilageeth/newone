package com.includehelp

abstract class PaintSheet {

    abstract var value:Int

    init {
        println("Init Block, Base Class")
    }

    open fun paint(){
        println("Paint Method , Base Class Implementation")
    }

    fun sketch(){
        println("Sketch Method , From Base Class!")
    }

    abstract fun draw()
}

class Painting : PaintSheet() {

    override var value=10

    init {
        println("Init Block, Child Class")

        super.paint()
    }

    override fun draw(){
        println("draw Method , override in Child Class")
    }

    override fun paint(){
        println("Paint Method , Child Class Implementation")
    }

    fun printValue(){
        println("Value : $value")
    }
}

fun main(args:Array<String>){

    val paint = Painting()

    paint.draw()

    paint.paint()

    paint.sketch()

    paint.printValue()
}
