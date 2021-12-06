<?php

require_once "Submarine.php";

class Submarine2 extends Submarine
{
    protected int $aim = 0;

    public function moveForward(int $value): self
    {
        $this->horizontal += $value;
        $this->depth += $this->aim * $value;

        return $this;
    }

    public function moveUp(int $value): self
    {
        $this->aim -= $value;

        return $this;
    }

    public function moveDown(int $value): self
    {
        $this->aim += $value;

        return $this;
    }
}
