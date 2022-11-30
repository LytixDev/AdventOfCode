#!/bin/bash
sed 's/ -> /,/' $1 | awk -F, '
$1 != $3 && $2 != $4 { next }
$1 > $3 { min = $3; max = $1; other = $2 }
$1 < $3 { min = $1; max = $3; other = $2 }
$1 != $3 { for ( i=min; i <= max; i++) { counter[i " " other]++ } }
$2 > $4 { min = $4; max = $2; other = $1 }
$2 < $4 { min = $2; max = $4; other = $1 }
$2 != $4 { for ( i=min; i <= max; i++) { counter[other " " i]++ } }
END { for (key in counter) { if(counter[key] >= 2) total++ } ; print total }'
