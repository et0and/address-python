# Changelog

## 0.1.0 (2026-05-12)

Full Changelog: [v0.0.2...v0.1.0](https://github.com/et0and/address-python/compare/v0.0.2...v0.1.0)

### Features

* **api:** api update ([2fe9781](https://github.com/et0and/address-python/commit/2fe9781487ad86e7bcf082b1b5cc5c249bad9780))
* **api:** api update ([afb4f9c](https://github.com/et0and/address-python/commit/afb4f9c8bbb07e3925b1de9040a158f4a6c682e9))
* **api:** api update ([332285d](https://github.com/et0and/address-python/commit/332285d7e13ac943fc9bb3070885bead5beace9f))
* **internal/types:** support eagerly validating pydantic iterators ([1631de1](https://github.com/et0and/address-python/commit/1631de1745af072f8541a9caa60018a53b9cb3b0))
* **internal:** implement indices array format for query and form serialization ([7ea569c](https://github.com/et0and/address-python/commit/7ea569c1e536d978598f419f0c8facf2886b9c3c))
* support setting headers via env ([6194f5f](https://github.com/et0and/address-python/commit/6194f5f76c37f61945193e70be901c25950fa5ce))


### Bug Fixes

* **client:** add missing f-string prefix in file type error message ([c8cacd1](https://github.com/et0and/address-python/commit/c8cacd1cd35f6aa5d60bbe3389ba15525d055347))
* **client:** preserve hardcoded query params when merging with user params ([0807f33](https://github.com/et0and/address-python/commit/0807f33daa7542dfee817f1c95460956cfd345ab))
* **deps:** bump minimum typing-extensions version ([2014dfc](https://github.com/et0and/address-python/commit/2014dfc6f45de1716750231b6262afc269cc0fa3))
* ensure file data are only sent as 1 parameter ([e524a6d](https://github.com/et0and/address-python/commit/e524a6df2c5db7198ba9d5834bd95192125e4af7))
* **pydantic:** do not pass `by_alias` unless set ([1839fea](https://github.com/et0and/address-python/commit/1839fea0249712f137d345049f1adc128aa5cd3e))
* sanitize endpoint path params ([011af81](https://github.com/et0and/address-python/commit/011af81112ccaf284def9a9b43e43039db4ee7cd))
* use correct field name format for multipart file arrays ([0dfae69](https://github.com/et0and/address-python/commit/0dfae691980e3ddf1601784ad4139be5d2db25b0))


### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([93846df](https://github.com/et0and/address-python/commit/93846dfde64024d4dc32bd490c29daa9bec3e4a1))


### Chores

* **ci:** skip lint on metadata-only changes ([0a66edb](https://github.com/et0and/address-python/commit/0a66edbd3809c620b943b301ffc7a6a0ec505770))
* **internal:** more robust bootstrap script ([9337320](https://github.com/et0and/address-python/commit/9337320d422668f9b19afefaf2ffbd0f1c962719))
* **internal:** reformat pyproject.toml ([d801e3e](https://github.com/et0and/address-python/commit/d801e3e7667d887083a2285fd5c797700925d60a))
* **internal:** tweak CI branches ([c41300b](https://github.com/et0and/address-python/commit/c41300b3a9197282ad8d2f61adb138fba5613667))
* **internal:** update gitignore ([dbae3a3](https://github.com/et0and/address-python/commit/dbae3a305052f8b04fd60fb99609e77eccc2eca3))

## 0.0.2 (2026-03-16)

Full Changelog: [v0.0.1...v0.0.2](https://github.com/et0and/address-python/compare/v0.0.1...v0.0.2)

### Chores

* configure new SDK language ([9d61f07](https://github.com/et0and/address-python/commit/9d61f07cf990e2064740ad99b31bf47cbeb84a27))
* update SDK settings ([4a0816c](https://github.com/et0and/address-python/commit/4a0816ccb07072073bfcb330fc093d53be4bd1ea))
* update SDK settings ([7c0d2c3](https://github.com/et0and/address-python/commit/7c0d2c31ddf0496a10e0911ef04439a953994445))
