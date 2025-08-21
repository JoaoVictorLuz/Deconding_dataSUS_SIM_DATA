with do_2023_2 as (

    select {{decode_fonte_da_informacao('FONTE_DA_INFORMACAO')}} AS FONTE_DA_INFORMACAO, count(*)
    from {{ ref('stg_2023') }}
    group by FONTE_DA_INFORMACAO
    ORDER BY 2
    
)

select * from do_2023_2

with do_2023_1 as (

    select OBITO_GRAVIDEZ, count(*)
    from {{ ref('stg_2023') }}
    group by OBITO_GRAVIDEZ
    ORDER BY 2
    
)

select * from do_2023_1