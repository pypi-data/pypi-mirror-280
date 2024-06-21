# System Bindings for libminimap2
Use this if you need lower-level bindings for minimap2. Also works with mm2-fast.

# Minimap2 Version
Currently this is synced to a recent git commit of minimap2. If you have other needs, let me know and I can make a branch and publish a corresponding version.

## Features 
* vendored - Regenerate the bindings from the vendored minimap2 source. Requires llvm installed. Useful to update the bindings to a different version of minimap2.
* mm2-fast - Use [mm2-fast](https://github.com/bwa-mem2/mm2-fast) as the backend rather than minimap2 itself.
* simde - Enable simde support (SIMD-everywhere)
* sse - Enable some sse bindings

## TODO
* Can we decouple from pthread? This would allow Windows and (possibly) WASM compilation.

## Changelog
### 0.1.15 minimap2.2.6
* Huge thanks to @leiste375 for aarch64 compilation!
* Better static linking support

### 0.1.14 minimap2.2.6
 * Fix regression by reverting to minimap2 release version

### 0.1.13 minimap2.2.26
 * Possible fixes for aarch64 compilation
 * Cleaner build system
 * Early support for cross crate for cross compilation

### 0.1.12 minimap2.2.26
 * Fix bug with SSE2/SSE4...
 
### 0.1.11 minimap2.2.26
* More transparent versioning of upstream minimap2
* Update minimap2-sys minimap2 to release 2.26
* minimap2-sys: update libc, bindgen deps
* Better sse support. Renamed sse flag to sse2only, sse4.1 is otherwise enabled by default (if detected)
* Hopefully better macos, aarch64, and NEON support

### 0.1.10
* Fix bug relating to compiling mm2-fast 

### 0.1.9
* Enable SIMD-everywhere compilation support

### 0.1.8
* Changed how zlib is compiled
* Dep versions update
* Added SSE compilation feature (Mostly autodetects)

### 0.1.7
* Make bindgen an optional feature
* zlib support for musl builds
