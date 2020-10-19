<?php
$shorted_array = [-2, 3, 4, 7, 8, 9, 11, 13];
$target = 11;
echo "Position of {$target} index is ". binary_search($shorted_array, $target);

function binary_search($arr, $target)
{
    $left = 0;
    $right = count($arr) - 1;

    while ($left <= $right) {
        $mid = floor(($left + $right) / 2);
        if ($arr[$mid] == $target) {
            return $mid;
        } elseif ($target < $arr[$mid]) {
            $right = $mid - 1;
        } else {
            $left = $mid+1;
        }
    }
    return -1;
}
