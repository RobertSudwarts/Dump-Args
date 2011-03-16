def dump_args(func):
	'''this decorator dumps (to STDOUT) the arguments passed to a function before the decorated function is called itself

	:usage:
		
		@dump_args
		def my_function(id, *args, **kw):
			print "dump_args will print 'id', 'args' and 'kw' before this line prints"
			print args
			print kw

	
	.. note:: this function is safe for use with Sphinx documentation. ``echo_func.__doc__ = func.__doc__`` does the magic
	'''
	argnames = func.func_code.co_varnames[:func.func_code.co_argcount]
	fname = func.func_name
	
	def echo_func(*args,**kw):
		spcr = "*" * 100
		print spcr
		print ":: called by [function] : " + fname + " ::"
		for arg, val in zip(argnames, args) + kw.items():
			if arg=="self":
				print arg, "=", type(val)
			else:
				print "%s=%r\t%s" % (arg, val, type(val))  # %r="raw"
			
		print spcr
		return func(*args, **kw)
	
	# forces the calling function's docstring for use in sphinx documentation
	echo_func.__doc__ = func.__doc__   
	
	return echo_func
