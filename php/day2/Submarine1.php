<?php

require_once "Submarine.php";

class Submarine1 extends Submarine
{
    public function moveForward(int $value): self
    {
       $this->horizontal += $value;

       return $this;
    }

    public function moveUp(int $value): self
    {
        $this->depth -= $value;

        return $this;
    }

    public function moveDown(int $value): self
    {
        $this->depth += $value;

        return $this;
    }
}
