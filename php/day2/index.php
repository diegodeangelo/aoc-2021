<?php

require_once "lib.php";
require_once "Submarine1.php";
require_once "Submarine2.php";

$commands = file("../../assets/day2/input.txt");

$submarine1 = parseCommands($commands, new Submarine1());

printf("Depth x Horizontal (Submarine1): %d\n", $submarine1->getDepth() * $submarine1->getHorizontal());

$submarine2 = parseCommands($commands, new Submarine2());

printf("Depth x Horizontal (Submarine2): %d\n", $submarine2->getDepth() * $submarine2->getHorizontal());
