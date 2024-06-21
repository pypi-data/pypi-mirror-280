# LibRDS
[![pipeline status](https://flerken.zapto.org:1115/kuba/librds/badges/main/pipeline.svg)](https://flerken.zapto.org:1115/kuba/librds/-/commits/main)


LibRDS is a simple library that you can use to generate and decode the RDS groups, just the groups, so something like `3000 2000 7575 7575` the origins of development of this started on 12 May, later creating the [rdPy](https://github.com/KubaPro010/rdPy) repository

Example code:
```python
import librds

basic = librds.GroupGenerator.basic(0x3000)
print(basic)

ps = librds.GroupGenerator.ps(basic,"hi",0)
print(ps)

print(librds.GroupDecoder.decode(ps))
```

Output:
```
    Group(a=12288, b=0, c=0, d=0, is_version_b=False)
    Group(a=12288, b=8, c=57549, d=26729, is_version_b=False)
    DecodedGroup(raw_group=Group(a=12288, b=8, c=57549, d=26729, is_version_b=False), pi=12288, tp=False, pty=0, group=GroupIdentifier(group_number=0, group_version=False), details=PSDetails(segment=0, di_stereo=None, di_artificial_head=None, di_compressed=None, di_dpty=False, ms=True, ta=False, text='hi', af=AlternativeFrequencyEntryDecoded(is_af=False, af_freq=None, af_freq1=None, lfmf_follows=None, all_af_lenght=None)))
```

**Note** that LibRDS required Python 3.10+ to run due to its use of `match`

# Decoder
LibRDS also includes a RDS Group decoder, so you can encode with librds and then also decode it, currently librds's decoder decodes all of the groups it can encode (such as CT, IH, TDC, etc...)