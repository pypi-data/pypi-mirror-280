## 1.27.1 - 2024-06-22
### Extractors
#### Additions
- [hentainexus] restore module ([#5275](https://github.com/mikf/gallery-dl/issues/5275), [#5712](https://github.com/mikf/gallery-dl/issues/5712))
- [shimmie2] support `vidya.pics` ([#5632](https://github.com/mikf/gallery-dl/issues/5632))
- [tcbscans] support other domains ([#5774](https://github.com/mikf/gallery-dl/issues/5774))
#### Fixes
- [deviantart] fix watching module ID extraction ([#5696](https://github.com/mikf/gallery-dl/issues/5696), [#5772](https://github.com/mikf/gallery-dl/issues/5772))
- [fanbox] handle KeyError for no longer existing plans ([#5759](https://github.com/mikf/gallery-dl/issues/5759))
- [kemonoparty:favorite] fix exception when sorting `null` objects ([#5692](https://github.com/mikf/gallery-dl/issues/5692). [#5721](https://github.com/mikf/gallery-dl/issues/5721))
- [skeb] fix `429 Too Many Requests` errors ([#5766](https://github.com/mikf/gallery-dl/issues/5766))
- [speakerdeck] fix extraction ([#5730](https://github.com/mikf/gallery-dl/issues/5730))
- [twitter] fix duplicate `ArkoseLogin` check
#### Improvements
- [nijie] support downloading videos ([#5707](https://github.com/mikf/gallery-dl/issues/5707), [#5617](https://github.com/mikf/gallery-dl/issues/5617))
- [philomena] support downloading `.svg` files ([#5643](https://github.com/mikf/gallery-dl/issues/5643))
- [szurubooru] support empty tag searches ([#5711](https://github.com/mikf/gallery-dl/issues/5711))
- [twitter] ignore `Unavailable` media ([#5736](https://github.com/mikf/gallery-dl/issues/5736))
#### Metadata
- [hitomi] extract `title_jpn` metadata ([#5706](https://github.com/mikf/gallery-dl/issues/5706))
- [instagram] extract `liked` metadata ([#5609](https://github.com/mikf/gallery-dl/issues/5609))
#### Options
- [newgrounds] extend `format` option ([#5709](https://github.com/mikf/gallery-dl/issues/5709))
- [twitter] extend `ratelimit` option ([#5532](https://github.com/mikf/gallery-dl/issues/5532))
- [twitter] add `username-alt` option ([#5715](https://github.com/mikf/gallery-dl/issues/5715))
#### Removals
- [photobucket] remove module
- [nitter] remove instances
- [vichan] remove `wikieat.club`
### Downloaders
- [ytdl] fix exception due to missing `ext` in unavailable videos ([#5675](https://github.com/mikf/gallery-dl/issues/5675))
### Formatter
- implement `C` format specifier ([#5647](https://github.com/mikf/gallery-dl/issues/5647))
- implement `X` format specifier ([#5770](https://github.com/mikf/gallery-dl/issues/5770))
### Options
- add `--no-input` command-line and `input` config option ([#5733](https://github.com/mikf/gallery-dl/issues/5733))
- add `--config-open` command-line option ([#5713](https://github.com/mikf/gallery-dl/issues/5713))
- add `--config-status` command-line option ([#5713](https://github.com/mikf/gallery-dl/issues/5713))
### Miscellaneous
- [actions] fix exception when `msg` is not a string ([#5683](https://github.com/mikf/gallery-dl/issues/5683))
