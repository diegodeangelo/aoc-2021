<?php

abstract class Submarine
{
    protected int $depth = 0;
    protected int $horizontal = 0;

    public function getDepth(): int
    {
        return $this->depth;
    }

    public function getHorizontal(): int
    {
        return $this->horizontal;
    }

    abstract public function moveForward(int $value): self;

    abstract public function moveUp(int $value): self;

    abstract public function moveDown(int $value): self;
}
