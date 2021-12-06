<?php

require_once "lib.php";
require_once "Submarine1.php";
require_once "Submarine2.php";

$commands = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"];

$submarine1 = parseCommands($commands, new Submarine1());

assert($submarine1->getHorizontal() == 15 && $submarine1->getDepth() == 10);

$submarine2 = parseCommands($commands, new Submarine2());

assert($submarine2->getHorizontal() == 15 && $submarine2->getDepth() == 60);
