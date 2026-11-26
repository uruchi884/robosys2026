#!/bin/bash
# SPDX-FileCopyrightText: 2026 Hayashi Masayuki
# SPDX-License-Identifier: BSD-3-Clause

ng () {
    echo "${1}行目のテスト失敗" >&2
    res=1
}

res=0

### NORMAL INPUT ###
out=$(printf 'time,value\n0,2\n1,4\n2,6\n' | ./csvstat 2)
[ "$?" = 0 ] || ng "$LINENO"
[ "$out" = '{"count": 3, "min": 2.0, "max": 6.0, "mean": 4.0, "rms": 4.320493798938574}' ] || ng "$LINENO"

### HEADER OPTION ###
out=$(printf 'value\n1\n3\n' | ./csvstat 1 --header)
[ "$?" = 0 ] || ng "$LINENO"
[ "$out" = '{"count": 2, "min": 1.0, "max": 3.0, "mean": 2.0, "rms": 2.23606797749979}' ] || ng "$LINENO"

### QUOTED CSV FIELD ###
out=$(printf 'sensor,"1.5"\nsensor,"2.5"\n' | ./csvstat 2)
[ "$?" = 0 ] || ng "$LINENO"
[ "$out" = '{"count": 2, "min": 1.5, "max": 2.5, "mean": 2.0, "rms": 2.0615528128088303}' ] || ng "$LINENO"

### EMPTY INPUT ###
out=$(./csvstat 1 </dev/null 2>/dev/null)
[ "$?" = 2 ] || ng "$LINENO"
[ "$out" = "" ] || ng "$LINENO"

### NON-NUMERIC INPUT ###
out=$(printf '1\nabc\n' | ./csvstat 1 2>/dev/null)
[ "$?" = 2 ] || ng "$LINENO"
[ "$out" = "" ] || ng "$LINENO"

### MISSING COLUMN ###
out=$(printf '1,2\n' | ./csvstat 3 2>/dev/null)
[ "$?" = 2 ] || ng "$LINENO"
[ "$out" = "" ] || ng "$LINENO"

### NON-FINITE INPUT ###
out=$(printf 'nan\n' | ./csvstat 1 2>/dev/null)
[ "$?" = 2 ] || ng "$LINENO"
[ "$out" = "" ] || ng "$LINENO"

### INVALID ARGUMENT ###
out=$(printf '1\n' | ./csvstat 0 2>/dev/null)
[ "$?" = 2 ] || ng "$LINENO"
[ "$out" = "" ] || ng "$LINENO"

[ "$res" = 0 ] && echo OK
exit "$res"
