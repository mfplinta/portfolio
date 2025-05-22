#!/bin/sh
exec nix develop --command python "$@"
