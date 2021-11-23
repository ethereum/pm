# Test quickstart states

The following quickstart states were generated via [`zcli`](http://github.com/protolambda/zcli) to be used as
references to test local quickstart implementations against.

## 16 Validors

Quickstart with 16 validators at 1567777777 genesis time.

`zcli` command:

```
zcli genesis mock --count 16 --genesis-time 1567777777 --keys interop/mocked_start/keygen_10000_validators.yaml
```

[SSZ output](./quickstart_genesis_16_1567777777.ssz)


## 32 Validors

Quickstart with 32 validators at 1567777777 genesis time.

`zcli` command:

```
zcli genesis mock --count 32 --genesis-time 1567777777 --keys interop/mocked_start/keygen_10000_validators.yaml
```

[SSZ output](./quickstart_genesis_32_1567777777.ssz)