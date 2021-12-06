<?php

require_once "Submarine.php";

function parseCommands(array $commands, Submarine $submarine): Submarine
{
    foreach ($commands as $command) {
        $instruction = explode(" ", $command);
        $operator = $instruction[0];
        $operand = $instruction[1];

        switch ($operator) {
            case "forward":
                $submarine->moveForward((int) $operand);
                break;
            case "up":
                $submarine->moveUp((int) $operand);
                break;
            case "down":
                $submarine->moveDown((int) $operand);
                break;
            default:
                throw new \Exception(sprintf("Operator %s not found!", $operator));
        }
    }

    return $submarine;
}
