{% macro decode_sexo(col) %}
    case {{col}}
        when '1' then 'masculino'
        when '2' then 'feminino'
        else 'ignorado'
    end
{% endmacro %}

{% macro decode_racacor(col) %}
    case trim({{col}})
        when '-' then 'ignorado'
        when '1' then 'branca'
        when '2' then 'preta'
        when '3' then 'amarela'
        when '4' then 'parda'
        when '5' then 'indigena'
    end
{% endmacro %}


{% macro decode_tipobito(col) %}
    case trim({{col}})
        when '1' then 'fetal'
        when '2' then 'nao_fetal'
    end
{% endmacro %}

{% macro decode_esc(col) %}
    case trim({{col}})
        when '1' then 'nenhuma'
        when '2' then '1 a 3 anos'
        when '3' then '4 a 7 anos'
        when '4' then '8 a 11 anos'
        when '8' then '8 a 11 anos'
        when '5' then '12 anos e mais'
        else 'ignorado'      
    end
{% endmacro %}

