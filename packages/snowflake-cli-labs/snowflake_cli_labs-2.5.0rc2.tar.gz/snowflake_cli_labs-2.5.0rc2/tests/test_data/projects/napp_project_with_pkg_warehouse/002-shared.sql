-- package script (2/2)

create or replace table {{ package_name }}.my_shared_content.shared_table (
  col1 number,
  col2 varchar
);
grant select on table {{ package_name }}.my_shared_content.shared_table
  to share in application package {{ package_name }};
