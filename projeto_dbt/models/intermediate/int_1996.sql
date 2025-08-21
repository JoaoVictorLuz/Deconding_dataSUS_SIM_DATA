with do_1996 as (
    select 
    {{decode_tipobito('TIPOBITO')}} as tipobito,
    {{decode_dt('DTOBITO')}} as dtobito,
    CODIGO_MUNICIPIO_NATURAL,
    {{decode_dt('DTNASC')}} as dtnasc,
    IDADE,
    {{decode_sexo('SEXO')}} as sexo,
    {{decode_racacor('RACACOR')}} as racacor,
    {{decode_estciv('ESTCIV')}} as estciv,
    {{decode_esc('ESC')}} as escolaridade,
    OCUP,
    CODIGO_MUNICIPIO_RESIDENCIA,
    {{decode_local_do_obito('LOCAL_DO_OBITO')}} as local_do_obito,
    CODIGO_MUNICIPIO_OBITO,
    cast(trim(IDADEMAE) as number(3,0)) as idademae,
    ESCOLARIDADE_DA_MAE,
    OCUPMAE,
    QTDFILVIVO,
    QTDFILMORT,
    TIPO_GRAVIDEZ,
    SEMANAS_DE_GESTACAO,
    TIPO_DE_PARTO,
    OBITOPARTO,
    PESO,
    OBITO_GRAVIDEZ,
    OBITOPUERP,
    ASSISTMED,
    FEZ_EXAME,
    FEZ_CIRURGIA,
    NECROPSIA,
    LINHAA,
    LINHAB,
    LINHAC,
    CID_LINHAD,
    LINHAII,
    CAUSABAS,
    TIPO_MORTE_NAO_NATURAL,
    ACIDTRAB,
    FONTE_DA_INFORMACAO
    from {{ ref('stg_1996') }}

)

select * from do_1996

