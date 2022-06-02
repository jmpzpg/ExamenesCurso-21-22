-- 1.- Hacer uno o varios triggers que cada vez que se haga una operación de inserción, modificación o borrado
-- en la tabla "employees" se guarde en la tabla "log_employees" una fila con la opración hecha y la fecha.

use empleados;
drop trigger if exists empleados_ins;
delimiter //

create trigger empleados_ins
before INSERT on employees 
for each ROW 
BEGIN 
	declare v_mensaje varchar(200) default '';
	set v_mensaje = concat('El usuario ', current_user(), ' ha hecho un INSERT en EMPLEADOS a las ',now() );
	insert into log_employees (mensaje)
		values (v_mensaje);
END//
delimiter ;

-- ---------------------------------- consulta de inserción -----------------------------------
insert into employees (first_name,last_name,email,phone_number,hire_date,job_id,salary,manager_id,department_id)
	values ('Pepe', 'Sánchez', 'ps@gmail.com', 555456789, '2010-04-15',1,25000,101,11);
-- --------------------------------------------------------------------------------------------

use empleados;
drop trigger if exists empleados_upd;
delimiter //

create trigger empleados_upd
before UPDATE on employees 
for each ROW 
BEGIN 
	declare v_mensaje varchar(600) default '';
	declare valores varchar(600) default '';
	
	set valores = concat('first_name: ',old.first_name, '-->', new.first_name,
						' last_name: ', old.last_name, '-->'  , new.last_name,
						' email: ', old.email,  '-->' , new.email,
						' phone_number: ', old.phone_number, '-->'  , new.phone_number,
						' hire_date: ', old.hire_date, '-->'  , new.hire_date,
						' job_id: ', old.job_id, '-->'  , new.job_id,
						' salary: ', old.salary,  '-->' , new.salary,
						' manager_id: ', old.manager_id, '-->'  , new.manager_id,
						' department_id: ', old.department_id, '-->'  , new.department_id);

	set v_mensaje = concat('El usuario ', current_user(), ' cambió ',valores,' en EMPLEADOS a las ',now() );
	insert into log_employees (mensaje)
		values (v_mensaje);
END//
delimiter ;


-- ---------------------------------- consulta de actualización -----------------------------------
update employees set salary = 35000 where employee_id = 207;
-- --------------------------------------------------------------------------------------------

use empleados;
drop trigger if exists empleados_del;
delimiter //

create trigger empleados_del
before delete on employees 
for each ROW 
BEGIN 
	declare v_mensaje varchar(200) default '';
	set v_mensaje = concat('El usuario ', current_user(), ' ha BORRADO el empleado con ID=', old.employee_id ,' en EMPLEADOS a las ',now() );
	insert into log_employees (mensaje)
		values (v_mensaje);
END//
delimiter ;


-- ---------------------------------- consulta de borrado -----------------------------------
DELETE from employees where employee_id = 208;
-- --------------------------------------------------------------------------------------------


-- 2.- Crea una función que tomando como parámetro el id del empleado devuelva el número de personas que 
-- dependen de dicho empleado.

-- select e.employee_id , count(d.dependent_id) from employees e join dependents d on e.employee_id = d.employee_id group by e.employee_id ;
-- select * from dependents d order by d.employee_id ;


drop function if exists num_dependientes;

DELIMITER //
CREATE FUNCTION num_dependientes(p_id int) RETURNS int reads sql data
BEGIN
	
	RETURN (select count(d.dependent_id) as Dependientes_a_su_cargo 
		from employees e join dependents d 
		on e.employee_id = d.employee_id 
		where e.employee_id = p_id);
	
END//

DELIMITER ;


select num_dependientes(102);



-- 3.- Usando la función anterior, hacer una consulta que muestre el nombre y el número de dependientes de cada empleado.

select CONCAT_WS(' ', e.first_name,e.last_name) as Nombre_empleado , 
				num_dependientes(e.employee_id) as Dependientes_a_su_cargo 
	from employees e join dependents d 
	on e.employee_id = d.employee_id 
	group by e.employee_id ;



-- 4.- Crear un procedimiento para rellenar una tabla de resumen de los empleados, utilizando cursores.
-- VER EJEMPLO !!!

select e.employee_id , e.manager_id , e.first_name , e2.employee_id , e2.first_name 
	from employees e join employees e2 
	on e.employee_id = e2.manager_id 
	where e.employee_id = 108
	
select e.employee_id , e.first_name , e.last_name , e.hire_date , e.email , 
	e.phone_number , e.salary , j.job_title , d.department_name , 
	concat(l.street_address, ' ', l.postal_code, ' ', l.city,  ' ', l.state_province, ' ', r.region_name)
	from employees e join jobs j on e.job_id = j.job_id 
	join departments d on d.department_id = e.department_id 
	join locations l on d.location_id = l.location_id 
	join countries c on l.country_id = c.country_id 
	join regions r on c.region_id = r.region_id ;

-- --------------------------

drop procedure if exists carga_tabla_resumen_empleados;

DELIMITER //
CREATE procedure carga_tabla_resumen_empleados()
begin
	
	declare v_fin_datos bool default false;
	declare v_id int;
	declare v_nombre varchar(20);
	declare v_apellido varchar(25);
	declare v_email varchar(100);
	declare v_phone varchar(20);
	declare v_fecha_cont date;
	declare v_sal decimal(8,2);
	declare v_nom_pu_tra varchar(100);
	declare v_nom_dep varchar(100);
	declare v_direccion varchar(100);


	declare mi_cursor cursor for
		select e.employee_id , concat(e.first_name ,' ', e.last_name) , e.hire_date , e.email , 
			e.phone_number , e.salary , j.job_title , d.department_name , 
			CONCAT_WS(' ',l.street_address, l.postal_code, l.city, l.state_province, r.region_name)
			from employees e join jobs j on e.job_id = j.job_id 
			join departments d on d.department_id = e.department_id 
			join locations l on d.location_id = l.location_id 
			join countries c on l.country_id = c.country_id 
			join regions r on c.region_id = r.region_id ;

	declare continue handler for not found set v_fin_datos = true;

	
	open mi_cursor;
	
--  recorrer el cursor	llenando la tabla resumen
	
	bucle_lectura: loop
		fetch mi_cursor into v_id, v_nombre, v_fecha_cont, v_email, v_phone, v_sal, v_nom_pu_tra,  v_nom_dep, v_direccion ;
		if v_fin_datos then
			leave bucle_lectura;
		end if;
	
		insert into resumen_employee (nombre_completo, datos_contacto, datos_empleo, datos_localizacion) 
				values (
			concat('El empleado ', v_nombre ,' con número ', v_id , ' fue contratado el ', v_fecha_cont ),
			concat('Su correo es ', v_email ,' y su teléfono ', v_phone ),
			concat('Trabaja como ', v_nom_pu_tra ,' en el departamento ',  v_nom_dep,' su manager es **** y gana un sueldo de ', v_sal),
			concat('El departamento ', v_nom_dep ,' se encuentra en la dirección: ' , v_direccion)
			) ;
	
	end loop;

	close mi_cursor;

	-- select * from resumen_employee re ;
	
end//
delimiter ;


call carga_tabla_resumen_empleados();


-- 5.- Crear un procedimiento para insertar un empleado (employee) y sus dependientes (dependents), dentro de una transacción.
-- NOTA: Los dependientes del empleado se toman de una tabla llamada cesta_dependientes, donde tendrán que ser introducidos previamente.


drop procedure if exists transaccion_empleado_dependientes;
delimiter //

create procedure transaccion_empleado_dependientes(fi_name varchar(20),
													la_name varchar(25),
													mail varchar(100),
													phone varchar(20),
													fecha date,
													job int,
													sal decimal(8,2),
													manager int,
													depart int,
													fallo bool)
begin
	declare v_new_id_empleado int default -1;
	declare MESSAGE_TEXT varchar(100) default 'Se ha producido un error en la transacción';

	declare exit handler for sqlexception
	begin
		rollback;
		select MESSAGE_TEXT;
	end;
	
	start transaction;
	
-- 1.- Insertar el nuevo empleado y recoger su id	
	
		insert into employees (first_name,last_name,email,phone_number,hire_date,job_id,salary,manager_id,department_id)
						values (fi_name, la_name, mail, phone, fecha, job, sal, manager, depart);
		set v_new_id_empleado = LAST_INSERT_ID() ;
		

-- 2.- Leer productos de la tabla cesta_dependientes: INSERT SELECT desde cesta_dependientes a tabla dependents
-- - Insertar las líneas de cesta_dependientes con ese id de empleado
	
		insert into dependents (first_name , last_name , relationship , employee_id )
		select cd.f_name , cd.l_name , cd.rel , v_new_id_empleado from cesta_dependientes cd;
	

-- 3.- Vaciar la cesta de dependientes

		TRUNCATE table cesta_dependientes ;

-- 6.- Si hay algún problema deshacemos la transacción
	
		if fallo then
			set MESSAGE_TEXT = 'Se produjo un error en la transacción y se disparó el Rollback';
			signal sqlstate '45000' ;
		end if;
	
	commit ;	
end//
delimiter ;



call transaccion_empleado_dependientes('Padre', 'Palotes', 'pp@gmail.com', 777456789, '2015-01-10',1,125000,101,11, TRUE);
